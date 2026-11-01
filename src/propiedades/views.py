from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Caracteristica, Propiedad, TipoPropiedad
from .serializers import (
    CaracteristicaSerializer,
    PropiedadPublicSerializer,
    PropiedadSerializer,
    TipoPropiedadSerializer,
)


class TipoPropiedadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoPropiedad.objects.all().order_by("id")
    serializer_class = TipoPropiedadSerializer
    permission_classes = [AllowAny]


class CaracteristicaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Caracteristica.objects.all().order_by("id")
    serializer_class = CaracteristicaSerializer
    permission_classes = [AllowAny]


class PropiedadViewSet(viewsets.ModelViewSet):
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
