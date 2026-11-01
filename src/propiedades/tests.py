from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from personas.models import Propietario
from ubicaciones.models import Barrio, Ciudad

from .models import Propiedad, TipoPropiedad


class PropiedadTests(APITestCase):
    def setUp(self):
        ciudad = Ciudad.objects.create(nombre="Rio Cuarto", provincia="Cordoba")
        self.barrio = Barrio.objects.create(nombre="Centro", ciudad=ciudad)
        self.tipo = TipoPropiedad.objects.create(nombre="Casa")
        self.propietario = Propietario.objects.create(
            nombre="Ana", apellido="Gomez", dni="30111222", telefono="358111"
        )
        self.propiedad = Propiedad.objects.create(
            titulo="Casa en Centro", direccion="San Martin 100", operacion="venta",
            precio=130000, superficie_m2=200, ambientes=4,
            barrio=self.barrio, tipo=self.tipo, propietario=self.propietario,
        )
        self.usuario = User.objects.create_user("pepe", password="1234")
        self.url = "/api/propiedades/"
        self.data = {
            "titulo": "Depto", "direccion": "Belgrano 50", "operacion": "alquiler",
            "superficie_m2": 50, "ambientes": 2,
            "barrio": self.barrio.id, "tipo": self.tipo.id, "propietario": self.propietario.id,
        }

    def test_list_propiedades_sin_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_propiedad_sin_auth(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_propiedad_con_auth(self):
        # autenticar primero
        self.client.login(username="pepe", password="1234")
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_solicitar_visita_sin_auth(self):
        data = {
            "nombre": "Luis", "apellido": "Diaz", "telefono": "358222",
            "email": "luis@mail.com", "fecha_hora": "2026-11-05T10:00",
        }
        response = self.client.post(f"{self.url}{self.propiedad.id}/solicitar_visita/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["estado"], "pendiente")
