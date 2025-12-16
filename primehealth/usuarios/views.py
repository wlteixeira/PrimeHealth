from django.shortcuts import render, redirect
from .forms import UsuarioForm

def cadastrar_usuario(request):
    formulario = UsuarioForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('/')

    return render(request, 'formulario.html', {
        'titulo': 'Cadastro de Usuário',
        'formulario': formulario,
        'url_voltar': '/'
    })
