from django.db import models
from django.contrib.auth.models import User

class Relatorio(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='relatorios'
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    data_geracao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Geração'
    )
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )

    def __str__(self):
        return self.titulo
