from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from .forms import MedicamentoForm

@login_required
def listar_medicamentos(request):
    medicamentos = Medicamento.objects.filter(usuario=request.user)

    itens = [{
        'campos': [m.nome, m.dosagem, m.horario],
        'url_editar': f'/medicamentos/editar/{m.id}/',
        'url_excluir': f'/medicamentos/excluir/{m.id}/'
    } for m in medicamentos]

    return render(request, 'listar_padrao.html', {
        'titulo': 'Medicamentos',
        'cabecalhos': ['Nome', 'Dosagem', 'Horário'],
        'itens': itens,
        'url_novo': '/medicamentos/novo/'
    })


@login_required
def cadastrar_medicamento(request):
    formulario = MedicamentoForm(request.POST or None)

    if formulario.is_valid():
        medicamento = formulario.save(commit=False)
        medicamento.usuario = request.user
        medicamento.save()
        return redirect('/medicamentos/')

    return render(request, 'formulario.html', {
        'titulo': 'Cadastrar Medicamento',
        'formulario': formulario,
        'url_voltar': '/medicamentos/'
    })


@login_required
def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id, usuario=request.user)
    formulario = MedicamentoForm(request.POST or None, instance=medicamento)

    if formulario.is_valid():
        formulario.save()
        return redirect('/medicamentos/')

    return render(request, 'formulario.html', {
        'titulo': 'Editar Medicamento',
        'formulario': formulario,
        'url_voltar': '/medicamentos/'
    })


@login_required
def excluir_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id, usuario=request.user)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('/medicamentos/')

    return render(request, 'confirmar_exclusao.html', {
        'url_voltar': '/medicamentos/'
    })
