from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from operaciones.serializers import VisitaSerializer
from personas.models import Cliente
from personas.serializers import ClienteSerializer

from .models import Caracteristica, Propiedad, TipoPropiedad
from .serializers import (
    CaracteristicaSerializer,
    PropiedadPublicSerializer,
    PropiedadSerializer,
    TipoPropiedadSerializer,
)


class TipoPropiedadViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Tipos de propiedad: casa, departamento, terreno... (publico, solo lectura).
    Para el filtro "Tipo" del buscador.
    """
    queryset = TipoPropiedad.objects.all().order_by("id")
    serializer_class = TipoPropiedadSerializer
    permission_classes = [AllowAny]


class CaracteristicaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Caracteristicas de las propiedades: pileta, quincho, patio... (publico,
    solo lectura). Para mostrarlas en la ficha y elegirlas al cargar una propiedad.
    """
    queryset = Caracteristica.objects.all().order_by("id")
    serializer_class = CaracteristicaSerializer
    permission_classes = [AllowAny]


class PropiedadViewSet(viewsets.ModelViewSet):
    """
    Propiedades de la inmobiliaria. El listado y la ficha son publicos;
    crear, editar y borrar requiere login.
    El listado trae barrio (con su ciudad), tipo, agente y caracteristicas
    anidados; el detalle y la carga usan los ids.
    Filtros: operacion, tipo, barrio, barrio__ciudad, dormitorios, ambientes,
    estado, precio__gte y precio__lte. Busqueda (search) por titulo, direccion
    y descripcion. Orden (ordering) por precio y fecha_publicacion.
    """
    queryset = Propiedad.objects.all().select_related("barrio__ciudad", "tipo", "agente").order_by("id")
    # listado y ficha publicos, la carga la hace el personal logueado
    permission_classes = [IsAuthenticatedOrReadOnly]
    # los mismos filtros que el buscador de Verdolini
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "operacion": ["exact"],
        "tipo": ["exact"],
        "barrio": ["exact"],
        "barrio__ciudad": ["exact"],
        "dormitorios": ["exact"],
        "ambientes": ["exact"],
        "estado": ["exact"],
        "precio": ["gte", "lte"],
    }
    search_fields = ["titulo", "direccion", "descripcion"]
    ordering_fields = ["precio", "fecha_publicacion"]

    def get_serializer_class(self):
        # anidado solo en el list, en el resto las FK van como id
        if self.action == "list":
            return PropiedadPublicSerializer
        return PropiedadSerializer

    # Endpoint: /api/propiedades/disponibles/
    @extend_schema(
        summary="Lista las propiedades disponibles",
        description=(
            "Devuelve solo las propiedades con estado disponible, paginadas de a 10. "
            "Los filtros del buscador no se aplican aca: para filtrar usar "
            "/api/propiedades/?estado=disponible."
        ),
        responses={200: PropiedadPublicSerializer(many=True)},
    )
    @action(detail=False, methods=["get"])
    def disponibles(self, request):
        propiedades = self.get_queryset().filter(estado="disponible")
        page = self.paginate_queryset(propiedades)
        serializer = PropiedadPublicSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    # Endpoint: /api/propiedades/<id>/solicitar_visita/
    # cualquier visitante puede pedir una visita, sin estar logueado
    @extend_schema(
        summary="Un visitante pide una visita a la propiedad",
        description=(
            "No hace falta estar logueado. Además de los datos del cliente se manda "
            "fecha_hora y comentarios. Si el cliente no existe (por email) se crea, "
            "y la visita queda pendiente con el agente de la propiedad."
        ),
        request=ClienteSerializer,
        responses={
            201: VisitaSerializer,
            400: OpenApiResponse(description="La propiedad no esta disponible o faltan datos"),
        },
    )
    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def solicitar_visita(self, request, pk=None):
        propiedad = self.get_object()
        if propiedad.estado != "disponible":
            return Response(
                {"mensaje": "La propiedad no esta disponible"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # si el cliente ya existe lo buscamos por el email, si no lo creamos
        cliente = Cliente.objects.filter(email=request.data.get("email")).first()
        if cliente is None:
            cliente_serializer = ClienteSerializer(data=request.data)
            if not cliente_serializer.is_valid():
                return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            cliente = cliente_serializer.save()

        visita_serializer = VisitaSerializer(data={
            "fecha_hora": request.data.get("fecha_hora"),
            "comentarios": request.data.get("comentarios", ""),
            "propiedad": propiedad.id,
            "cliente": cliente.id,
            "agente": propiedad.agente_id,
        })
        if not visita_serializer.is_valid():
            return Response(visita_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        visita_serializer.save()
        return Response(visita_serializer.data, status=status.HTTP_201_CREATED)
