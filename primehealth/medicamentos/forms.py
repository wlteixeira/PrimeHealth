from django import forms
from .models import Medicamento

class MedicamentoFormulario(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'dosagem', 'horario']
