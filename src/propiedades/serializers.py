from rest_framework import serializers

from personas.serializers import AgenteSerializer
from ubicaciones.models import Barrio
from ubicaciones.serializers import CiudadSerializer

from .models import Caracteristica, Propiedad, TipoPropiedad


class TipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPropiedad
        fields = "__all__"
        read_only_fields = ["id"]


class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = "__all__"
        read_only_fields = ["id"]


class BarrioPublicSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(read_only=True)

    class Meta:
        model = Barrio
        fields = ["id", "nombre", "ciudad"]


class PropiedadPublicSerializer(serializers.ModelSerializer):
    # para el list: trae los datos completos para la tarjeta del front
    barrio = BarrioPublicSerializer(read_only=True)
    tipo = TipoPropiedadSerializer(read_only=True)
    agente = AgenteSerializer(read_only=True)
    caracteristicas = CaracteristicaSerializer(many=True, read_only=True)

    class Meta:
        model = Propiedad
        fields = "__all__"
        read_only_fields = ["id", "fecha_publicacion"]


class PropiedadSerializer(serializers.ModelSerializer):
    # para crear, editar y el detalle: las FK van como id
    class Meta:
        model = Propiedad
        fields = "__all__"
        read_only_fields = ["id", "fecha_publicacion"]
