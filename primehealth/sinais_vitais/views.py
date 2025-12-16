from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import SinalVital
from .forms import SinalVitalForm

@login_required
def listar_sinais_vitais(request):
    sinais = SinalVital.objects.filter(usuario=request.user)

    itens = [{
        'campos': [s.tipo, s.valor, s.data_registro],
        'url_editar': f'/sinais-vitais/editar/{s.id}/',
        'url_excluir': f'/sinais-vitais/excluir/{s.id}/'
    } for s in sinais]

    return render(request, 'listar_padrao.html', {
        'titulo': 'Sinais Vitais',
        'cabecalhos': ['Tipo', 'Valor', 'Data'],
        'itens': itens,
        'url_novo': '/sinais-vitais/novo/'
    })


@login_required
def cadastrar_sinal_vital(request):
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
        'url_voltar': '/sinais-vitais/'
    })
