from django.contrib import admin

from .models import Contrato, Visita


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ("propiedad", "cliente", "fecha_hora", "estado", "agente")
    list_filter = ("estado", "agente", "fecha_hora")
    search_fields = ("propiedad__titulo", "cliente__apellido", "cliente__email")


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ("propiedad", "cliente", "tipo", "monto", "fecha_inicio", "fecha_fin", "activo", "agente")
    list_filter = ("tipo", "activo", "agente")
    search_fields = ("propiedad__titulo", "cliente__apellido", "cliente__dni")
