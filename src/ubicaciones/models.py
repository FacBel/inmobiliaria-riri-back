from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.provincia}"


class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name="barrios")

    def __str__(self):
        return f"{self.nombre} ({self.ciudad.nombre})"
