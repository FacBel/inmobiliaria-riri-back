from django.db import models

from personas.models import Agente, Cliente
from propiedades.models import Propiedad

ESTADOS_VISITA = [
    ("pendiente", "Pendiente"),
    ("confirmada", "Confirmada"),
    ("cancelada", "Cancelada"),
    ("realizada", "Realizada"),
]
TIPOS_CONTRATO = [("venta", "Venta"), ("alquiler", "Alquiler")]


class Visita(models.Model):
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADOS_VISITA, default="pendiente")
    comentarios = models.TextField(blank=True)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name="visitas")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="visitas")
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True, blank=True, related_name="visitas")

    def __str__(self):
        return f"Visita a {self.propiedad} - {self.cliente}"


class Contrato(models.Model):
    tipo = models.CharField(max_length=10, choices=TIPOS_CONTRATO)
    fecha_inicio = models.DateTimeField()
    # la venta no tiene fecha de fin
    fecha_fin = models.DateTimeField(null=True, blank=True)
    monto = models.IntegerField()
    activo = models.BooleanField(default=True)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name="contratos")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="contratos")
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True, blank=True, related_name="contratos")

    def __str__(self):
        return f"Contrato de {self.tipo} - {self.propiedad}"
