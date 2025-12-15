from django import forms
from .models import SinalVital

class SinalVitalFormulario(forms.ModelForm):
    class Meta:
        model = SinalVital
        fields = [
            'pressao_arterial',
            'glicemia',
            'peso',
            'frequencia_cardiaca'
        ]
