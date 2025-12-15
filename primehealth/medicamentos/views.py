from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Medicamento
from .forms import MedicamentoFormulario

@login_required
def listar_medicamentos(request):
    medicamentos = Medicamento.objects.filter(usuario=request.user)
    return render(request, 'medicamentos/listar.html', {'medicamentos': medicamentos})

@login_required
def cadastrar_medicamento(request):
    formulario = MedicamentoFormulario(request.POST or None)
    if formulario.is_valid():
        medicamento = formulario.save(commit=False)
        medicamento.usuario = request.user
        medicamento.save()
        return redirect('listar_medicamentos')
    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id, usuario=request.user)
    formulario = MedicamentoFormulario(request.POST or None, instance=medicamento)
    if formulario.is_valid():
        formulario.save()
        return redirect('listar_medicamentos')
    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def excluir_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id, usuario=request.user)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('listar_medicamentos')
    return render(request, 'confirmar_exclusao.html', {'objeto': medicamento})
