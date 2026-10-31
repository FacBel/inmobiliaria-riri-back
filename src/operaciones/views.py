from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contrato, Visita
from .serializers import ContratoPublicSerializer, ContratoSerializer, VisitaSerializer


class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all().select_related("propiedad", "cliente", "agente").order_by("id")
    serializer_class = VisitaSerializer
    permission_classes = [IsAuthenticated]


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all().select_related("propiedad", "cliente", "agente").order_by("id")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # anidado solo en el list, en el resto las FK van como id
        if self.action == "list":
            return ContratoPublicSerializer
        return ContratoSerializer
