from datetime import timedelta
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

        data = self.cleaned_data['data']

        data_anterior = data - timedelta(days=1)
        data_posterior = data + timedelta(days=1)

        coletas_existentes = Coleta.objects.filter(data__range=[data_anterior, data_posterior])
        if (len(coletas_existentes) > 0  ):
            raise ValidationError("Já há um produto deste fornecedor com este nome cadastrado.")
