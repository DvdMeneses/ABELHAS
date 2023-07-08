"""
URL configuration for prova-GQS-3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Producao.views import criar_coleta, editar_coleta, listar_coletas, Listar_Coletas_lv, \
    detalhes_coleta, Detalhes_coleta_dv, Criar_coleta_cv, deletar_coleta, Deletar_coleta_dv, exibir_coletas, \
    Exibir_Coletas_lv

app_name = "producao"

urlpatterns = [
    path('adicionar/', criar_coleta, name='adicionar'),
    path('adicionar_cv/', Criar_coleta_cv.as_view(), name='adicionar_cv'),
    path('editar/<int:coleta_id>/', editar_coleta, name='editar'),
    path('listar/', listar_coletas, name='listar'),
    path('listar_lv/', Listar_Coletas_lv.as_view(), name='listar_lv'),
    path('exibir/', exibir_coletas, name='exibir'),
    path('exibir_lv/', Exibir_Coletas_lv.as_view(), name='exibir_lv'),
    path('detalhes/<int:pk>/', detalhes_coleta, name='detalhes'),
    path('detalhes_dv/<int:pk>/', Detalhes_coleta_dv.as_view(), name='detalhes_dv'),
    path('deletar/<int:pk>/', deletar_coleta, name='deletar'),
    path('deletar_dv/<int:pk>/', Deletar_coleta_dv.as_view(), name='deletar_dv'),

]