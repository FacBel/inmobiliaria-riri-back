from rest_framework import serializers

from personas.serializers import ClienteSerializer
from propiedades.serializers import PropiedadSerializer

from .models import Contrato, Visita


class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = "__all__"
        read_only_fields = ["id"]


class ContratoPublicSerializer(serializers.ModelSerializer):
    # para el list: muestra la propiedad y el cliente completos
    propiedad = PropiedadSerializer(read_only=True)
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Contrato
        fields = "__all__"
        read_only_fields = ["id"]


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = "__all__"
        read_only_fields = ["id"]
