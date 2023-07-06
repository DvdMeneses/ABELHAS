from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm


def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            data = form.cleaned_data['data']
            criacao = form.cleaned_data['criacao']
            quantidade = form.cleaned_data['quantidade']
            Coleta.objects.create(
                id=id,
                data=data,
                criacao=criacao,
                quantidade=quantidade
            )
            return redirect('coleta:listar')
    else:
        form = ColetaForm()
    informacoes = {
        'form': form
    }
    return render(request, 'coleta/adicionar.html', informacoes)

class Criar_Produto_cv(CreateView):
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


class CriarColeta(CreateView):
    model = Coleta
    form_class = ColetaForm
    template_name = 'coleta/index.html'
    success_url = reverse_lazy('coleta:listar_coletas')

def listar_coletas(request):
    lista_coletas = Coleta.objects.all()

    informacoes = {
        'lista_coletas': lista_coletas
    }

    return render(request, 'coleta/listar_coletas.html', informacoes)

class ListarColetas(ListView):
    model = Coleta
    context_object_name = 'lista_coletas'
    template_name = 'coleta/listar_coletas.html'