from django.contrib import admin

from .models import Barrio, Ciudad


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "provincia")
    search_fields = ("nombre",)


@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad")
    list_filter = ("ciudad",)
    search_fields = ("nombre",)
