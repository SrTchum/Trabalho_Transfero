from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm

# Create your views here.

# def cadastro(request):
#     return render(
#         request,
#         'cadastro.html',
#     )

def login(request):
    return render(
        request,
        'usuarios/login.html',
    )

def criarUsuario(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # Redireciona para a página de login após o cadastro
            return redirect('usuario/login')

    else: 
        form = UsuarioForm()

    return render(
        request,
        'usuarios/cadastrar.html',
        {'form': form}
    )
