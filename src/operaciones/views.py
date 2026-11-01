from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Contrato, Visita
from .serializers import ContratoPublicSerializer, ContratoSerializer, VisitaSerializer


class VisitaViewSet(viewsets.ModelViewSet):
    """
    Visitas a propiedades (requiere login). Gestion interna: el visitante la
    pide desde la propiedad (queda pendiente) y el personal la confirma.
    """
    queryset = Visita.objects.all().select_related("propiedad", "cliente", "agente").order_by("id")
    serializer_class = VisitaSerializer
    permission_classes = [IsAuthenticated]

    # Endpoint: /api/visitas/<id>/confirmar/
    @extend_schema(
        summary="El personal confirma una visita",
        description="Pasa la visita de pendiente a confirmada. Requiere estar logueado.",
        request=None,
        responses={
            200: OpenApiResponse(description="Visita confirmada"),
            400: OpenApiResponse(description="La visita no esta pendiente"),
        },
    )
    @action(detail=True, methods=["post"])
    def confirmar(self, request, pk=None):
        visita = self.get_object()
        if visita.estado != "pendiente":
            return Response(
                {"mensaje": "Solo se puede confirmar una visita pendiente"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        visita.estado = "confirmada"
        visita.save()
        return Response({"mensaje": "Visita confirmada"})


class ContratoViewSet(viewsets.ModelViewSet):
    """
    Contratos de venta y alquiler (requiere login). Gestion interna.
    El listado trae la propiedad y el cliente anidados; el detalle y la carga
    usan los ids.
    """
    queryset = Contrato.objects.all().select_related("propiedad", "cliente", "agente").order_by("id")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # anidado solo en el list, en el resto las FK van como id
        if self.action == "list":
            return ContratoPublicSerializer
        return ContratoSerializer
