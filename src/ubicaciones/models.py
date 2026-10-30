from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "ciudades"

    def __str__(self):
        return f"{self.nombre}, {self.provincia}"


class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    # PROTECT: no se puede borrar una ciudad que tiene barrios cargados
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, related_name="barrios")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.ciudad.nombre})"
