# Create your views here.
from django.shortcuts import render, redirect
from .models import Animal
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import AnimalForm
from django.contrib.auth import logout

@login_required
def listar_animais(request):
    animais = Animal.objects.all()
    return render(request, 'listar_animais.html', {'animais': animais})

@login_required
def adicionar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_animais')
    else:
        form = AnimalForm()
    return render(request, 'adicionar_animal.html', {'form': form})

@login_required
def atualizar_animal(request, pk):
    produto = get_object_or_404(Animal, pk=pk)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = AnimalForm(instance=Animal)
    
    return render(request, 'atualizar_animal.html', {'form': form, 'animal': Animal})

@login_required
def detalhes_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'detalhes_Animal.html', {'Animal': animal})

@login_required
def excluir_animal(request, pk):
    produto = get_object_or_404(Animal, pk=pk)
    if request.method in ['POST', 'GET']:
        produto.delete()
    return redirect('listar_animais')



def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return render(request, 'login.html')
    else:
        return render (request, 'login.html')
    
@login_required
def custom_logout(request):
    logout (request)
    return redirect('login')

@login_required
def home_page(request):
    return render(request, 'home.html')