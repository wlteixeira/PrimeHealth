from django.db import models
from django.contrib.auth.models import User

class Medicamento(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='medicamentos'
    )
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome'
    )
    dosagem = models.CharField(
        max_length=50,
        verbose_name='Dosagem'
    )
    horario = models.TimeField(
        verbose_name='Horário'
    )

    def __str__(self):
        return f'{self.nome} - {self.dosagem}'
