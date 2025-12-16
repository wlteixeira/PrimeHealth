from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sintoma
from .forms import SintomaForm


@login_required
def listar_sintomas(request):
    sintomas = Sintoma.objects.filter(usuario=request.user)
    return render(request, 'listar_sintomas.html', {
        'sintomas': sintomas
    })


@login_required
def criar_sintoma(request):
    formulario = SintomaForm(request.POST or None)

    if formulario.is_valid():
        sintoma = formulario.save(commit=False)
        sintoma.usuario = request.user
        sintoma.save()
        return redirect('/sintomas/')

    return render(request, 'formulario.html', {
        'titulo': 'Cadastrar Sintoma',
        'formulario': formulario,
        'url_voltar': '/sintomas/'
    })


@login_required
def editar_sintoma(request, id):
    sintoma = get_object_or_404(Sintoma, id=id, usuario=request.user)
    formulario = SintomaForm(request.POST or None, instance=sintoma)

    if formulario.is_valid():
        formulario.save()
        return redirect('/sintomas/')

    return render(request, 'formulario.html', {
        'titulo': 'Editar Sintoma',
        'formulario': formulario,
        'url_voltar': '/sintomas/'
    })


@login_required
def excluir_sintoma(request, id):
    sintoma = get_object_or_404(Sintoma, id=id, usuario=request.user)

    if request.method == 'POST':
        sintoma.delete()
        return redirect('/sintomas/')

    return render(request, 'confirmar_exclusao.html', {
        'objeto': sintoma,
        'url_voltar': '/sintomas/'
    })
