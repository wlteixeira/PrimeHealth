from django.db import models
from django.contrib.auth.models import User

class SinalVital(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sinais_vitais'
    )
    pressao_arterial = models.CharField(max_length=7)
    glicemia = models.FloatField()
    peso = models.FloatField()
    frequencia_cardiaca = models.IntegerField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sinais Vitais - {self.usuario.username}"
