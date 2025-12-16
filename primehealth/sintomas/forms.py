from django import forms
from .models import Sintoma

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = ['nome', 'intensidade']

