from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Especie, Animal
from .forms import CustomUserCreationForm
from django.core.exceptions import ValidationError

#TESTANDO AS VIEWS
class AnimalViewsTestCase(TestCase):


    def setUp(self):
        """Configuração inicial antes dos testes"""
        # Criando usuário com todos os campos necessários
        self.user = User.objects.create_user(
            username="testeuser",
            email="teste@exemplo.com",
            password="testesenha123"
        )

        # Logando o usuário
        self.client.login(username="testeuser", password="testesenha123")

        # Criando uma espécie e um animal para os testes
        self.especie_gato = Especie.objects.create(nome="Gato")
        self.animal = Animal.objects.create(
            nome="Simba",
            idade_em_meses=6,
            raca="Persa",
            descricao="Pelagem longa e dócil",
            sexo="M",
            especie=self.especie_gato,
        )

    def test_view_lista_animais(self):
        """Testa se a página de listagem de animais retorna status 200"""
        url = reverse("listar_animais")  
        response = self.client.get(url)
        print(f"Status code lista_animais: {response.status_code}")  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Simba") 

    def test_view_detalhe_animal(self):
        """Testa se a página de detalhes do animal retorna status 200"""
        url = reverse("detalhes_animal", args=[self.animal.id])
        response = self.client.get(url)
        print(f"Status code detalhe_animal: {response.status_code}") 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pelagem longa e dócil")

#TESTANDO OS FORMS
class CustomUserCreationFormTest(TestCase):
    def test_form_valid(self):
        """Testa se o formulário é válido quando preenchido corretamente"""
        form_data = {
            "username": "usuario_teste",
            "email": "usuario@email.com",
            "password1": "TesteSenha123",
            "password2": "TesteSenha123",
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())  

    def test_form_invalid_password_mismatch(self):
        """Testa se o formulário é inválido quando as senhas não correspondem"""
        form_data = {
            "username": "usuario_teste",
            "email": "usuario@email.com",
            "password1": "TesteSenha123",
            "password2": "SenhaErrada",
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)  

    def test_form_invalid_missing_email(self):
        """Testa se o formulário é inválido quando falta o e-mail"""
        form_data = {
            "username": "usuario_teste",
            "password1": "TesteSenha123",
            "password2": "TesteSenha123",
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid()) 
        self.assertIn("email", form.errors)  

#TESTANDO AS MODELS
class AnimalModelValidationTest(TestCase):


    def setUp(self):
        self.especie = Especie.objects.create(nome="Cachorro")

    def test_idade_negativa_invalida(self):
        """Testa se uma idade negativa gera erro de validação"""
        animal = Animal(
            nome="Bolt",
            idade_em_meses=-1,  
            raca="Labrador",
            descricao="Energia pura!",
            sexo="M",
            especie=self.especie
        )
        with self.assertRaises(ValidationError) as context:
            animal.full_clean() 
        self.assertIn("A idade não pode ser negativa.", str(context.exception))

    def test_idade_maior_que_maximo(self):
        """Testa se uma idade acima de 240 meses gera erro de validação"""
        animal = Animal(
            nome="Rex",
            idade_em_meses=241, 
            raca="Pastor Alemão",
            descricao="Muito protetor!",
            sexo="M",
            especie=self.especie
        )
        with self.assertRaises(ValidationError) as context:
            animal.full_clean()  
        self.assertIn("A idade máxima permitida é 240 meses (20 anos).", str(context.exception))

    def test_idade_valida(self):
        """Testa se uma idade dentro do intervalo permitido passa na validação"""
        animal = Animal(
            nome="Luna",
            idade_em_meses=120, 
            raca="Poodle",
            descricao="Muito brincalhona!",
            sexo="F",
            especie=self.especie
        )
        try:
            animal.full_clean() 
        except ValidationError:
            self.fail("full_clean() levantou ValidationError inesperadamente!")