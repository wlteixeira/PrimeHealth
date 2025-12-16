from django.db import models
from django.contrib.auth.models import User

class Sintoma(models.Model):

    INTENSIDADES = [
        ('Leve', 'Leve'),
        ('Moderado', 'Moderado'),
        ('Grave', 'Grave'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=100)
    intensidade = models.CharField(
        max_length=10,
        choices=INTENSIDADES
    )
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.intensidade})'
