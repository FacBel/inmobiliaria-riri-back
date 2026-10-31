from rest_framework import serializers

from .models import Agente, Cliente, Propietario


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = "__all__"
        read_only_fields = ["id"]


class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = "__all__"
        read_only_fields = ["id"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        read_only_fields = ["id"]
