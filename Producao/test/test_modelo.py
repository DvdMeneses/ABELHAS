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
        criacao2 = Criacao.objects.create(raca="africana", data_entrada='2021-01-19')
        criacao3 = Criacao.objects.create(raca="real", data_entrada='2020-02-18')

        Coleta.objects.create(quantidade=20, data='2023-09-10', criacao=criacao)
        Coleta.objects.create(quantidade=5, data='2023-10-10', criacao=criacao)
        Coleta.objects.create(quantidade=14, data='2023-11-09', criacao=criacao)
        Coleta.objects.create(quantidade=12, data='2023-12-12', criacao=criacao)



    # test de tamanho de caracteres
    def test_tamanho_caracteres(self):
        coleta = Coleta.objects.get(id=1)
        raca = coleta.criacao.raca
        tamanho_max = coleta.criacao._meta.get_field('raca').max_length
        self.assertTrue(len(str(raca)) <= tamanho_max)

    # test de obrigatoriedade de colea
    def test_campos_obrigatorios_coleta(self):
        coleta = Coleta.objects.get(id=1)
        data = coleta.data
        quantidade = coleta.quantidade
        self.assertTrue(data != None)
        self.assertTrue(quantidade != None)

    # test de obrigatoriedade de criacao
    def test_campo_obrigatorio_criacao(self):
        criacao = Criacao.objects.get(id=1)
        self.assertIsNotNone(criacao.raca, 'Campo de Raca nao pode ser nulo')
        self.assertIsNotNone(criacao.data_entrada, "Campo de data nao pode ser nulo")

    # test de verbose name
    def test_verbose_name(self):
        coleta = Coleta.objects.get(id=1)
        criacao = coleta._meta.get_field('criacao')
        data = coleta._meta.get_field('data')
        quantidade = coleta._meta.get_field('quantidade')
        self.assertEqual(criacao.verbose_name, 'criacao')
        self.assertEqual(data.verbose_name, 'data')
        self.assertEqual(quantidade.verbose_name, 'quantidade')

    # teste de ordenacao
    def test_ordenacao_coletas(self):
        coleta1 = Coleta.objects.get(id=1)
        coleta2 = Coleta.objects.get(id=2)
        coleta3 = Coleta.objects.get(id=3)
        coleta4 = Coleta.objects.get(id=4)
        coletas = [coleta1, coleta2, coleta3,coleta4]
        coletas_ordenadas = list(Coleta.objects.all())

        self.assertEqual(coletas_ordenadas, coletas)