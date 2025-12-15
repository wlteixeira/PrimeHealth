from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sintoma
from .forms import SintomaFormulario

@login_required
def listar_sintomas(request):
    sintomas = Sintoma.objects.filter(usuario=request.user)
    return render(request, 'sintomas/listar.html', {'sintomas': sintomas})

@login_required
def cadastrar_sintoma(request):
    formulario = SintomaFormulario(request.POST or None)
    if formulario.is_valid():
        sintoma = formulario.save(commit=False)
        sintoma.usuario = request.user
        sintoma.save()
        return redirect('listar_sintomas')
    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def editar_sintoma(request, id):
    sintoma = get_object_or_404(Sintoma, id=id, usuario=request.user)
    formulario = SintomaFormulario(request.POST or None, instance=sintoma)
    if formulario.is_valid():
        formulario.save()
        return redirect('listar_sintomas')
    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def excluir_sintoma(request, id):
    sintoma = get_object_or_404(Sintoma, id=id, usuario=request.user)
    if request.method == 'POST':
        sintoma.delete()
        return redirect('listar_sintomas')
    return render(request, 'confirmar_exclusao.html', {'objeto': sintoma})
