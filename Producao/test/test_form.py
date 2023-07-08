from datetime import date

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from Producao.forms import ColetaForm
from Producao.models import Coleta, Criacao


class ProdutoFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Apis mellifera', data_entrada='2023-04-20')
        Criacao.objects.create(raca='Apis mellifera mellifera', data_entrada='2020-11-22')
        Criacao.objects.create(raca='Apis mellifera ligustica', data_entrada='2022-03-07')
        Criacao.objects.create(raca='Caucasica', data_entrada='2021-05-27')
        Criacao.objects.create(raca='Apis mellifera carnica da Eslovênia', data_entrada='2023-01-11')
        Criacao.objects.create(raca='Apis mellifera scutellata', data_entrada='2019-03-11')

        Coleta.objects.create(criacao=Criacao.objects.get(id=1), data='2023-04-20', quantidade=3)
        Coleta.objects.create(criacao=Criacao.objects.get(id=3), data='2022-03-07', quantidade=2)
        Coleta.objects.create(criacao=Criacao.objects.get(id=1), data='2021-05-27', quantidade=5)
        Coleta.objects.create(criacao=Criacao.objects.get(id=2), data='2023-01-02', quantidade=1)

    def test_coleta_existente1(self):
        form = ColetaForm(
            data = {
                'criacao': Criacao.objects.get(id=1),
                'data': '2023-04-20',
                'quantidade': 3
            }
        )
        self.assertTrue(form.is_valid())

    def test_coleta_existente2(self):
        form = ColetaForm(
            data = {
                'criacao': Criacao.objects.get(id=1),
                'data': '2023-04-21',
                'quantidade': 3
            }
        )
        self.assertTrue(form.is_valid())