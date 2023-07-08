from datetime import date

from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Producao.models import Coleta, Criacao
from Producao import views

class ColetaViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Apis mellifera', data_entrada='2023-04-20')
        Criacao.objects.create(raca='Apis mellifera ', data_entrada='2020-11-22')
        Criacao.objects.create(raca='Apis mellifera ligustica', data_entrada='2022-03-07')
        Criacao.objects.create(raca='Caucasica', data_entrada='2021-05-27')
        Criacao.objects.create(raca='Apis mellifera carnica da Eslovênia', data_entrada='2023-01-11')
        Criacao.objects.create(raca='Apis mellifera scutellata', data_entrada='2019-03-11')

        Coleta.objects.create(criacao=Criacao.objects.get(id=1), data='2023-04-20', quantidade=3)
        Coleta.objects.create(criacao=Criacao.objects.get(id=3), data='2022-03-07', quantidade=2)
        Coleta.objects.create(criacao=Criacao.objects.get(id=1), data='2021-05-27', quantidade=5)
        Coleta.objects.create(criacao=Criacao.objects.get(id=2), data='2023-01-02', quantidade=1)

    def setUp(self):
        usuario = User.objects.create_user(username='user0', password='123')
        usuario.save()


    # deletar
        # Deletar Coleta

    # Teste para a url correta
    def test_deletar_coleta_url(self):
        coleta1 = Coleta.objects.get(id=1)
        url = reverse('deletar', args=[coleta1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_deletar_coleta_template(self):
        coleta1 = Coleta.objects.get(id=1)
        url = reverse('deletar', args=[coleta1.pk])
        response = self.client.post(url)
        self.assertTemplateUsed(response, 'coleta/deletar.html')

        def test_deletar_coleta_objeto_correto(self):
            coleta1 = Coleta.objects.get(id=1)
            url = reverse('deletar', args=[coleta1.pk])
            self.client.post(url)
            deleted_coleta = Coleta.objects.filter(id=coleta1.pk)
            self.assertIsNone(deleted_coleta)


    # Cria corretamente o objeto
    def test_criar_coleta(self):
        criacao = Criacao.objects.get(id=1)
        criacao2 = Criacao.objects.get(id=1)
        url = reverse('adicionar')
        data = {
            'criacao': criacao2.pk,  # Use o atributo 'pk' para obter o ID do objeto Criacao
            'data': '2023-06-28',
            'quantidade': 5,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        coleta = Coleta.objects.last()  # Get the newly created object
        self.assertEqual(coleta.criacao, criacao)
        self.assertEqual(coleta.data, date(2023, 6, 28))
        self.assertEqual(coleta.quantidade, 5)



    # Teste para detalhes de coleta
    def test_detalhes_coleta_url(self):
        coleta1 = Coleta.objects.get(id=1)
        url = reverse('detalhes', args=[coleta1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detalhes_coleta_template(self):
            coleta1 = Coleta.objects.get(id=1)
            url = reverse('detalhes', args=[coleta1.pk])
            response = self.client.get(url)
            self.assertTemplateUsed(response, 'coleta/detalhes.html')

    def test_detalhes_coleta_atributos(self):
        coleta1 = Coleta.objects.get(id=1)
        url = reverse('detalhes', args=[coleta1.pk])
        response = self.client.get(url)
        self.assertEqual(response.context['coleta'], coleta1)

    #LISTAR
    def test_listar_coleta_url(self):
        response = self.client.get(reverse('listar'))
        self.assertEquals(response.status_code, 200)

    def test_listar_coleta_all(self):
        response = self.client.get(reverse('listar'))
        self.assertEqual(len(response.context['listar']), 4)

    def test_listar_coleta_template(self):
        response = self.client.get(reverse('listar'))
        self.assertTemplateUsed(response, 'coleta/listar.html')

        # Testes para: Exibir relatório de coleta

        # URL está correta

    def test_exibir_relatorio_coleta_url(self):
        url = reverse('exibir')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Usa o template correto

    def test_exibir_relatorio_coleta_template(self):
        url = reverse('exibir')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'coleta/exibir.html')



    def relatorio_colet(self):
        response = self.client.get(reverse('exibir'))
        self.assertEquals(response.context['exibir'], [[2, 2023, 10], [1, 2023, 5]])