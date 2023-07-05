from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from Producao.forms import ColetaForm
from Producao.models import Coleta, Criacao


class ProdutoFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coleta.objects.create(quantidada_Coleta="20 Litros", data="10/09/2023", criacao="mosquito")

    def test_coleta_existente(self):
        form = ColetaForm(data={'quantidada_Coleta': '20 Litros', 'data': '10/09/2023', 'criacao': "mosquito"})
        self.assertFalse(form.is_valid())

    def test_coleta_existente(self):
        form = ColetaForm(data={'quantidada_Coleta': '13 Litros', 'data': '11/09/2023', 'criacao': "mosquito"})
        self.assertFalse(form.is_valid())
    def test_coleta_fornecedor_nao_existente_1(self):
        form = ColetaForm(data={'quantidada_Coleta': '7 Litros', 'fornecedor': '12/09/2023',  'criacao': "mosquito"})
        self.assertTrue(form.is_valid())

    def test_coleta_fornecedor_nao_existente_2(self):
        form = ColetaForm(data={'quantidade-coleta': '10 Litros', 'data': '15/02/2023', 'criacao': "africana"})
        self.assertTrue(form.is_valid())