from django import forms
from .models import SinalVital

class SinalVitalForm(forms.ModelForm):
    class Meta:
        model = SinalVital
        fields = ['tipo', 'valor', 'data_registro']
        labels = {
            'tipo': 'Tipo do Sinal Vital',
            'valor': 'Valor',
            'data_registro': 'Data do Registro'
        }
        widgets = {
            'tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Pressão Arterial'
            }),
            'valor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 120/80'
            }),
            'data_registro': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
