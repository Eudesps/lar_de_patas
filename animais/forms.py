from django import forms
from .models import Animal, Especie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EspecieForm (forms.ModelForm): 
    class Meta: 
        model = Especie 
        fields = ['nome']   

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'idade_em_meses', 'raca', 'descricao', 'sexo', 'especie']
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
                'rows': 4,  
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select',
            }),
            'especie': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(
        required=True,  # Agora o campo é obrigatório
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail',
        })
    )
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome de usuário',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None
          