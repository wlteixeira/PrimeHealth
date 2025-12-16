from django.db import models
from django.contrib.auth.models import User

class SinalVital(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sinais_vitais'
    )
    tipo = models.CharField(
        max_length=100,
        verbose_name='Tipo'
    )
    valor = models.CharField(
        max_length=50,
        verbose_name='Valor'
    )
    data_registro = models.DateField(
        verbose_name='Data do Registro'
    )

    def __str__(self):
        return f'{self.tipo}: {self.valor}'
