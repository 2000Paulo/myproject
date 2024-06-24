# myapp/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Objeto
from .models import MeuObjeto
from .forms import ObjetoForm
from .forms import MeuObjetoForm
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')


# @login_required
def home(request):
    return render(request, 'myapp/home.html')


# Função para criar objeto
def criar_objeto(request):
    if request.method == 'POST':
        form = MeuObjetoForm(request.POST)
        if form.is_valid():
            novo_objeto = form.save()  # Salva o objeto no banco de dados
            return redirect('home')
    else:
        form = MeuObjetoForm()
    
    return render(request, 'myapp/create.html', {'form': form})


def mostrar_objeto(request):
    objetos = MeuObjeto.objects.all()
    return render(request, 'myapp/list.html', {'objetos': objetos})

# Função para excluir objeto (já existente)
def deletar_objeto(request, objeto_id):
    objeto = get_object_or_404(MeuObjeto, id=objeto_id)
    if request.method == 'POST':
        objeto.delete()
        return redirect('mostrar_objeto')
    return render(request, 'myapp/delete.html', {'objeto': objeto})

# Função para atualizar objeto (nova)
def atualizar_objeto(request, objeto_id):
    objeto = get_object_or_404(MeuObjeto, id=objeto_id)
    if request.method == 'POST':
        form = MeuObjetoForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect('mostrar_objeto')
    else:
        form = MeuObjetoForm(instance=objeto)
    return render(request, 'myapp/update.html', {'form': form, 'objeto': objeto})

#Redirecionar para Fastapi

def redirect_to_fastapi(request):
    return HttpResponseRedirect("http://localhost:8001/")
