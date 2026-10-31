from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # el dni se completa si despues firma un contrato
    dni = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=30)
    # con el email lo buscamos cuando pide una visita desde la web
    email = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
