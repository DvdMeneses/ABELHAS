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
            criacao = form.cleaned_data['criacao']
            data = form.cleaned_data['data']
            quantidade = form.cleaned_data['quantidade']

            Coleta.objects.create(
                criacao=criacao,
                data=data,
                quantidade=quantidade
            )
            return redirect('coleta:index.html')

    else:
        form = ColetaForm()

    informacoes = {
        'form': form
    }

    return render(request, 'coleta/index.html', informacoes)


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