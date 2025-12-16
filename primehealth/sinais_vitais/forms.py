from django import forms
from .models import SinalVital

class SinalVitalForm(forms.ModelForm):
    class Meta:
        model = SinalVital
        fields = ['tipo', 'valor']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
        }
