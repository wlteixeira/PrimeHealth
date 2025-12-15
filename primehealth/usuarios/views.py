from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def cadastrar_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('painel_saude')
    else:
        formulario = UserCreationForm()

    return render(request, 'usuarios/cadastro.html', {'formulario': formulario})
