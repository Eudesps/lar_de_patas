# Create your views here.
from django.shortcuts import render, redirect
from .models import Animal

def listar_animais(request):
    animais = Animal.objects.all()
    return render(request, 'listar_animais.html', {'animais': animais})

from .forms import AnimalForm
def adicionar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_animais')
    else:
        form = AnimalForm()
    return render(request, 'adicionar_animal.html', {'form': form})

from django.shortcuts import get_object_or_404

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

from django.shortcuts import render, get_object_or_404

def detalhes_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'detalhes_Animal.html', {'Animal': animal})

def excluir_animal(request, pk):
    produto = get_object_or_404(Animal, pk=pk)
    if request.method in ['POST', 'GET']:
        produto.delete()
    return redirect('listar_animais')