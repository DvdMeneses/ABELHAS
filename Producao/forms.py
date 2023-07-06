from multiprocessing import connection

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Producao.models import Coleta

class ColetaForm(ModelForm):
    class Meta:
        model = Coleta
        fields = ['id', 'data', 'criacao', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()
        # Pega o nome que foi adicionado no formulário
        id = cleaned_data.get("id")
        quantidade = self.cleaned_data['quantidade']
        coletas_existentes = Coleta.objects.filter(id=id, quantidade=quantidade)
        if (len(coletas_existentes) > 0):
            raise ValidationError("Já há um produto deste fornecedor com este nome cadastrado.")