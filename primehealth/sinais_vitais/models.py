from django.db import models
from django.contrib.auth.models import User

class SinalVital(models.Model):

    TIPOS = [
        ('Pressão Arterial', 'Pressão Arterial'),
        ('Frequência Cardíaca', 'Frequência Cardíaca'),
        ('Temperatura', 'Temperatura'),
        ('Saturação', 'Saturação'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(
        max_length=30,
        choices=TIPOS
    )
    valor = models.CharField(max_length=20)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} - {self.valor}'
