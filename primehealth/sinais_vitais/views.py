from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SinalVital
from .forms import SinalVitalFormulario

@login_required
def listar_sinais_vitais(request):
    sinais = SinalVital.objects.filter(usuario=request.user)
    return render(request, 'sinais_vitais/listar.html', {'sinais': sinais})

@login_required
def cadastrar_sinal_vital(request):
    formulario = SinalVitalFormulario(request.POST or None)
    if formulario.is_valid():
        sinal = formulario.save(commit=False)
        sinal.usuario = request.user
        sinal.save()
        return redirect('listar_sinais_vitais')
    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def editar_sinal_vital(request, id):
    sinal = get_object_or_404(SinalVital, id=id, usuario=request.user)
    formulario = SinalVitalFormulario(request.POST or None, instance=sinal)
    if formulario.is_valid():
        formulario.save()
        return redirect('listar_sinais_vitais')
    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def excluir_sinal_vital(request, id):
    sinal = get_object_or_404(SinalVital, id=id, usuario=request.user)
    if request.method == 'POST':
        sinal.delete()
        return redirect('listar_sinais_vitais')
    return render(request, 'confirmar_exclusao.html', {'objeto': sinal})
