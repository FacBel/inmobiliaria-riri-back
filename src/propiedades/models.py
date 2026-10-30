from django.db import models

from personas.models import Agente, Propietario
from ubicaciones.models import Barrio

OPERACIONES = [("venta", "Venta"), ("alquiler", "Alquiler")]
MONEDAS = [("ARS", "Pesos"), ("USD", "Dólares")]
ESTADOS = [
    ("disponible", "Disponible"),
    ("reservada", "Reservada"),
    ("alquilada", "Alquilada"),
    ("vendida", "Vendida"),
]


class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Caracteristica(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=150)
    operacion = models.CharField(max_length=10, choices=OPERACIONES)
    # si no tiene precio en el front se muestra "Consultar"
    precio = models.IntegerField(null=True, blank=True)
    moneda = models.CharField(max_length=3, choices=MONEDAS, default="USD")
    superficie_m2 = models.IntegerField()
    ambientes = models.IntegerField()
    dormitorios = models.IntegerField(default=0)
    banios = models.IntegerField(default=0)
    cocheras = models.IntegerField(default=0)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="disponible")
    foto = models.ImageField(upload_to="propiedades/", blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name="propiedades")
    tipo = models.ForeignKey(TipoPropiedad, on_delete=models.CASCADE, related_name="propiedades")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="propiedades")
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True, blank=True, related_name="propiedades")
    caracteristicas = models.ManyToManyField(Caracteristica, blank=True, related_name="propiedades")

    def __str__(self):
        return self.titulo
