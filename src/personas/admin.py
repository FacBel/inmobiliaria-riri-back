from django.contrib import admin

from .models import Agente, Cliente, Propietario


@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "telefono", "email")
    search_fields = ("apellido", "nombre", "dni")


@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "telefono", "matricula")
    search_fields = ("apellido", "nombre", "matricula")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "telefono", "email")
    # filtra por sus visitas y contratos (related_name)
    list_filter = ("visitas__estado", "contratos__tipo")
    search_fields = ("apellido", "nombre", "dni", "email")
