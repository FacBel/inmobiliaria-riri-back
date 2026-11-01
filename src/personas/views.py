from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Agente, Cliente, Propietario
from .serializers import AgenteSerializer, ClienteSerializer, PropietarioSerializer


class PropietarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Propietarios (requiere login, solo lectura). Para el desplegable al cargar
    una propiedad. El alta se hace desde el admin.
    """
    queryset = Propietario.objects.all().order_by("id")
    serializer_class = PropietarioSerializer
    # datos privados, solo para el personal
    permission_classes = [IsAuthenticated]


class AgenteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Agentes de la inmobiliaria (publico, solo lectura). Para el "Contactar
    operador" de la ficha y el desplegable al cargar una propiedad.
    """
    queryset = Agente.objects.all().order_by("id")
    serializer_class = AgenteSerializer
    # publico para el "Contactar operador" del front
    permission_classes = [AllowAny]


class ClienteViewSet(viewsets.ModelViewSet):
    """
    Clientes (requiere login). Gestion interna del personal. Los clientes
    tambien se crean solos cuando un visitante pide una visita.
    """
    queryset = Cliente.objects.all().order_by("id")
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
