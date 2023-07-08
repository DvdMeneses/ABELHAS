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
from django.contrib import admin
from django.urls import path
from Producao.views import criar_coleta, editar_coleta, listar_coletas, Listar_Coletas_lv, \
    detalhes_coleta, Detalhes_coleta_dv, Criar_coleta_cv, deletar_coleta, Deletar_coleta_dv, exibir_coletas, \
    Exibir_Coletas_lv




urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar-coleta/', views.criar_coleta, name='criar-coleta'),
    path('listar-coletas/', views.listar_coletas, name='listar_coletas'),

]
