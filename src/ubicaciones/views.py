from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Barrio, Ciudad
from .serializers import BarrioSerializer, CiudadSerializer


class CiudadViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Ciudades (publico, solo lectura). Para el filtro "Localidad" del buscador.
    """
    queryset = Ciudad.objects.all().order_by("id")
    serializer_class = CiudadSerializer
    permission_classes = [AllowAny]


class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Barrios (publico, solo lectura). Para el filtro "Barrio" del buscador;
    cada barrio trae el id de su ciudad.
    """
    queryset = Barrio.objects.all().select_related("ciudad").order_by("id")
    serializer_class = BarrioSerializer
    permission_classes = [AllowAny]
