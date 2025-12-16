from django.db import models
from django.contrib.auth.models import User

class Sintoma(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sintomas'
    )
    descricao = models.CharField(
        max_length=255,
        verbose_name='Descrição'
    )
    data_registro = models.DateField(
        verbose_name='Data do Registro'
    )

    def __str__(self):
        return f'{self.descricao} ({self.usuario.username})'
