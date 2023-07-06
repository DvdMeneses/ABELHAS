from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Producao.models import Coleta, Criacao
from Producao import views

class ColetaViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coleta.objects.create(criacao='', data='20/04/2023', quantidade=3)
        Coleta.objects.create(criacao='', data='07/03/2022', quantidade=2)
        Coleta.objects.create(criacao='', data='27/05/2021', quantidade=5)
        Coleta.objects.create(criacao='', data='02/01/2023', quantidade=1)

    def setUp(self):
        usuario = User.objects.create_user(username='user0', password='123')
        usuario.save()

    def test_listar_coleta_url(self):
        response = self.client.get(reverse('listar'))
        self.assertEquals(response.status_code, 200)

    def test_listar_coleta_template(self):
        response = self.client.get(reverse('listar'))
        self.assertTemplateUsed(response, 'coleta/listar.html')

    def test_listar_coleta_all(self):
        response = self.client.get(reverse('listar'))
        self.assertEqual(len(response.context['listar']), 4)
