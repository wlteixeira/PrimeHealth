from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SinalVital
from .forms import SinalVitalForm


@login_required
def listar_sinais_vitais(request):
    sinais = SinalVital.objects.filter(usuario=request.user)
    return render(request, 'listar_sinais.html', {
        'sinais': sinais
    })


@login_required
def criar_sinal_vital(request):
    formulario = SinalVitalForm(request.POST or None)

    if formulario.is_valid():
        sinal = formulario.save(commit=False)
        sinal.usuario = request.user
        sinal.save()
        return redirect('/sinais-vitais/')

    return render(request, 'formulario.html', {
        'titulo': 'Cadastrar Sinal Vital',
        'formulario': formulario,
        'url_voltar': '/sinais-vitais/'
    })


@login_required
def editar_sinal_vital(request, id):
    sinal = get_object_or_404(SinalVital, id=id, usuario=request.user)
    formulario = SinalVitalForm(request.POST or None, instance=sinal)

    if formulario.is_valid():
        formulario.save()
        return redirect('/sinais-vitais/')

    return render(request, 'formulario.html', {
        'titulo': 'Editar Sinal Vital',
        'formulario': formulario,
        'url_voltar': '/sinais-vitais/'
    })


@login_required
def excluir_sinal_vital(request, id):
    sinal = get_object_or_404(SinalVital, id=id, usuario=request.user)

    if request.method == 'POST':
        sinal.delete()
        return redirect('/sinais-vitais/')

    return render(request, 'confirmar_exclusao.html', {
        'objeto': sinal,
        'url_voltar': '/sinais-vitais/'
    })
