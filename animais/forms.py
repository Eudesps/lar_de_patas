from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'idade_em_meses', 'raca', 'descricao', 'sexo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do animal',
            }),
            'idade_em_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a idade em meses',
            }),
            'raca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a raça',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição do animal',
                'rows': 4,  # Número de linhas do campo de texto
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
