from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Agente, Cliente, Propietario
from .serializers import AgenteSerializer, ClienteSerializer, PropietarioSerializer


class PropietarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Propietario.objects.all().order_by("id")
    serializer_class = PropietarioSerializer
    # datos privados, solo para el personal
    permission_classes = [IsAuthenticated]


class AgenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agente.objects.all().order_by("id")
    serializer_class = AgenteSerializer
    # publico para el "Contactar operador" del front
    permission_classes = [AllowAny]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("id")
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
