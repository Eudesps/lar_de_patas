from django.db import models
from django.core.exceptions import ValidationError

def validar_idade_em_meses(value):
    if value < 0:
        raise ValidationError("A idade não pode ser negativa.")
    if value > 240:
        raise ValidationError("A idade máxima permitida é 240 meses (20 anos).")

class Especie(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    #A idade deve ser colocada em meses, considerando que a probalidade de ser 
    #cadastrado um filhote com meses de idade é maior que um animal com anos de idade
    idade_em_meses = models.IntegerField(validators=[validar_idade_em_meses], default=0 ) # idade em meses do animal
    raca = models.CharField(max_length=100)
    descricao = models.TextField()
    sexo = models.CharField(
        max_length=1,
        choices=[("M", "Macho"), ("F", "Fêmea")],
        default="M",
    )
    especie =  models.ForeignKey (Especie, on_delete=models.CASCADE) 