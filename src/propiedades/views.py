from rest_framework import viewsets

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


class CaracteristicaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Caracteristica.objects.all().order_by("id")
    serializer_class = CaracteristicaSerializer


class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all().select_related("barrio__ciudad", "tipo", "agente").order_by("id")

    def get_serializer_class(self):
        # anidado solo en el list, en el resto las FK van como id
        if self.action == "list":
            return PropiedadPublicSerializer
        return PropiedadSerializer
