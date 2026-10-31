from rest_framework import serializers

from .models import Barrio, Ciudad


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"
        read_only_fields = ["id"]


class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = "__all__"
        read_only_fields = ["id"]
