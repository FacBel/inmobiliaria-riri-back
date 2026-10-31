from rest_framework.routers import DefaultRouter

from operaciones.views import ContratoViewSet, VisitaViewSet
from personas.views import AgenteViewSet, ClienteViewSet, PropietarioViewSet
from propiedades.views import CaracteristicaViewSet, PropiedadViewSet, TipoPropiedadViewSet
from ubicaciones.views import BarrioViewSet, CiudadViewSet

router = DefaultRouter()

router.register("ciudades", CiudadViewSet, basename="ciudades")
router.register("barrios", BarrioViewSet, basename="barrios")
router.register("tipos-propiedad", TipoPropiedadViewSet, basename="tipos-propiedad")
router.register("caracteristicas", CaracteristicaViewSet, basename="caracteristicas")
router.register("agentes", AgenteViewSet, basename="agentes")
router.register("propietarios", PropietarioViewSet, basename="propietarios")
router.register("propiedades", PropiedadViewSet, basename="propiedades")
router.register("clientes", ClienteViewSet, basename="clientes")
router.register("visitas", VisitaViewSet, basename="visitas")
router.register("contratos", ContratoViewSet, basename="contratos")
