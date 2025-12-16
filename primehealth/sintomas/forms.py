from django import forms
from .models import Sintoma

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = ['descricao', 'data_registro']
        labels = {
            'descricao': 'Descrição do Sintoma',
            'data_registro': 'Data do Registro'
        }
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Dor de cabeça'
            }),
            'data_registro': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
