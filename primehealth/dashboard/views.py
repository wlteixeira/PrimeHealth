from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sintomas.models import Sintoma
from sinais_vitais.models import SinalVital

@login_required
def painel_saude(request):
    sintomas = Sintoma.objects.filter(usuario=request.user)
    sinais_vitais = SinalVital.objects.filter(usuario=request.user)

    return render(request, 'painel.html', {
        'sintomas': sintomas,
        'sinais_vitais': sinais_vitais
    })
