from django.db import models
from datetime import date



class Criacao(models.Model):
    id = models.AutoField(primary_key=True)
    raca = models.CharField(max_length=30)
    data_entrada = models.DateField(default=date.today)
    def __str__(self):
        return self.raca

    class Meta:
        ordering = ['data_entrada', 'raca']


class Coleta(models.Model):
    id = models.AutoField(primary_key=True)
    criacao = models.ForeignKey(Criacao, on_delete=models.CASCADE, verbose_name ='criacao')
    data = models.DateField(default=date.today)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Coleta - ID: {self.pk}"

    class Meta:
        ordering = ['data', 'quantidade']
