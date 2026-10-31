from django.contrib import admin

from .models import Caracteristica, Propiedad, TipoPropiedad


@admin.register(TipoPropiedad)
class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "operacion", "barrio", "precio", "moneda", "estado", "agente", "fecha_publicacion")
    # los mismos filtros que el buscador de la web
    list_filter = ("operacion", "tipo", "estado", "barrio__ciudad", "barrio", "caracteristicas")
    search_fields = ("titulo", "direccion", "descripcion")
