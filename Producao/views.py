from collections import namedtuple
from multiprocessing import connection
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm


def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            criacao = form.cleaned_data['criacao']
            quantidade = form.cleaned_data['quantidade']
            Coleta.objects.create(
                data=data,
                criacao=criacao,
                quantidade=quantidade
            )
            return redirect('listar')
    else:
        form = ColetaForm()
    informacoes = {
        'form': form
    }
    return render(request, 'coleta/adicionar.html', informacoes)

class Criar_coleta_cv(CreateView):
    model = Coleta
    form_class = ColetaForm
    template_name = 'Coleta/criar_coleta.html'
    success_url = reverse_lazy('coleta:listar')


def editar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)

    if request.method == 'POST':
        form = ColetaForm(request.POST, instance=coleta)
        if form.is_valid():
            form.save()
            return redirect('coleta:listar')
    else:
        form = ColetaForm(instance=coleta)

    informacoes = {
        'form': form
    }
    return render(request, 'coleta/editar.html', informacoes)

def listar_coletas(request):
    lista_coletas = Coleta.objects.all()

    informacoes = {
        'listar': lista_coletas
    }

    return render(request, 'coleta/listar.html', informacoes)


class Listar_Coletas_lv(ListView):
    model = Coleta
    # Definir nome, senão será usado "object"
    context_object_name = 'lista_coletas'
    template_name = 'coleta/listar_coletas.html'

class Detalhes_coleta_dv(DetailView):
    model = Coleta
    context_object_name = 'coleta'
    template_name = 'coleta/detalhes_coleta.html'

def detalhes_coleta(request, pk):
    coleta = Coleta.objects.get(pk=pk)
    informacoes = {
        'coleta': coleta
    }
    return render(request, 'coleta/detalhes.html', informacoes)


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def deletar_coleta(request, pk):
    coleta = Coleta.objects.get(pk=pk)
    informacoes = {
        'coleta': coleta
    }
    return render(request, 'coleta/deletar.html', informacoes)


class Deletar_coleta_dv(DeleteView):
    # Indicar o nome do produto que quer ser deletado
    model = Coleta
    # Indicar o template que será utilizado
    template_name = "Coleta/deletar_coleta.html"
    # Página para redirecionamento
    success_url = reverse_lazy('produto:listar')

def exibir_coletas(request):
    exibir_coletas = Coleta.objects.all()

    informacoes = {
        'exibir': exibir_coletas
    }

    return render(request, 'coleta/exibir.html', informacoes)

class Exibir_Coletas_lv(ListView):
    model = Coleta
    # Definir nome, senão será usado "object"
    context_object_name = 'exibir_coletas'
    template_name = 'coleta/exibir_coletas.html'



