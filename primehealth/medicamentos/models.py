from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Medicamento(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='medicamentos'
    )
    nome = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50)
    horario = models.TimeField(null=True, blank=True)

    def clean(self):
        if not self.horario:
            raise ValidationError(
                'É obrigatório definir um horário para o medicamento.'
            )

    def __str__(self):
        return f"{self.nome} - {self.dosagem}"
