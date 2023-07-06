from django.test import TestCase
from Producao.models import Criacao, Coleta


class CriacaoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Apis mellifera', data_entrada='2023-04-20')
        Criacao.objects.create(raca='Apis mellifera mellifera', data_entrada='2029-03-06')
        Criacao.objects.create(raca='Apis mellifera ligustica', data_entrada='2022-03-07')
        Criacao.objects.create(raca='Caucasica', data_entrada='2021-05-27')
        Criacao.objects.create(raca='Apis mellifera carnica da Eslovênia', data_entrada='2023-02-01')
        Criacao.objects.create(raca='Apis mellifera scutellata', data_entrada='2025-05-22')

    def test_tamanho_caracteres(self):
        criacao = Criacao.objects.get(id=1)
        raca = criacao.raca
        tamanho_max = criacao._meta.get_field('raca').max_length
        self.assertTrue(len(raca) <= tamanho_max)

    def test_campos_obrigatorios(self):
        criacao = Criacao.objects.get(id=1)
        raca = criacao.raca
        data = criacao.data_entrada
        self.assertTrue(raca != '')
        self.assertTrue(data != None)

    def test_verbose_name(self):
        criacao = Criacao.objects.get(id=1)
        raca = criacao._meta.get_field('raca')
        data = criacao._meta.get_field('data_entrada')
        self.assertEqual(raca.verbose_name, 'raca')
        self.assertEqual(data.verbose_name, 'data entrada')


class ColetaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        criacao = Criacao.objects.create(raca='Mosquito', data_entrada='2023-09-10')
        Coleta.objects.create(id = 1,quantidade=20, data='2023-09-10', criacao=criacao)
        Coleta.objects.create(id = 2,quantidade=5, data='2023-10-10', criacao=criacao)
        Coleta.objects.create(id = 3,quantidade=14, data='2023-11-09', criacao=criacao)
        Coleta.objects.create(id = 4,quantidade=12, data='2023-12-12', criacao=criacao)

    def test_tamanho_caracteres(self):
        coleta = Coleta.objects.get(id=1)
        raca = coleta.criacao.raca
        tamanho_max = coleta.criacao._meta.get_field('raca').max_length
        self.assertTrue(len(str(raca)) <= tamanho_max)

    def test_campos_obrigatorios(self):
        coleta = Coleta.objects.get(id=1)
        data = coleta.data
        quantidade = coleta.quantidade
        self.assertTrue(data != None)
        self.assertTrue(quantidade != None)

    def test_verbose_name(self):
        coleta = Coleta.objects.get(id=1)
        criacao = coleta._meta.get_field('criacao')
        data = coleta._meta.get_field('data')
        quantidade = coleta._meta.get_field('quantidade')
        self.assertEqual(criacao.verbose_name, 'criacao')
        self.assertEqual(data.verbose_name, 'data')
        self.assertEqual(quantidade.verbose_name, 'quantidade')
