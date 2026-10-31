from rest_framework import viewsets

from .models import Agente, Cliente, Propietario
from .serializers import AgenteSerializer, ClienteSerializer, PropietarioSerializer


class PropietarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Propietario.objects.all().order_by("id")
    serializer_class = PropietarioSerializer


class AgenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agente.objects.all().order_by("id")
    serializer_class = AgenteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("id")
    serializer_class = ClienteSerializer
