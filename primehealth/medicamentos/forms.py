from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'dosagem', 'horario']
        labels = {
            'nome': 'Nome do Medicamento',
            'dosagem': 'Dosagem',
            'horario': 'Horário'
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Paracetamol'
            }),
            'dosagem': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 500mg'
            }),
            'horario': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            })
        }
