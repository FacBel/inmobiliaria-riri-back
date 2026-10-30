from django.contrib.auth.models import User
from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Agente(models.Model):
    # cada agente es un usuario del sistema, así puede loguearse
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agente")
    telefono = models.CharField(max_length=30)
    matricula = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["user__last_name"]

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # el dni lo completa la inmobiliaria si se firma un contrato
    dni = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=30)
    # el email identifica al cliente cuando pide una visita desde la web
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
