from django import forms
from .models import Sintoma

class SintomaFormulario(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = ['nome', 'intensidade', 'observacoes']
