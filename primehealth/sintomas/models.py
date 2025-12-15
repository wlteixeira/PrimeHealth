from django.db import models
from django.contrib.auth.models import User

class Sintoma(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sintomas'
    )
    nome = models.CharField(max_length=100)
    intensidade = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)]
    )
    data_registro = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} - Intensidade {self.intensidade}"
