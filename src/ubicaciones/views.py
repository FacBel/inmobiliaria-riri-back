from rest_framework import viewsets

from .models import Barrio, Ciudad
from .serializers import BarrioSerializer, CiudadSerializer


class CiudadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ciudad.objects.all().order_by("id")
    serializer_class = CiudadSerializer


class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all().select_related("ciudad").order_by("id")
    serializer_class = BarrioSerializer
