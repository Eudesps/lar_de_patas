from django.db import models
from django.core.exceptions import ValidationError

def validar_idade_em_meses(value):
    if value < 0:
        raise ValidationError("A idade não pode ser negativa.")
    if value > 240:
        raise ValidationError("A idade máxima permitida é 240 meses (20 anos).")

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
    )  # Sexo do Animal 


#COMANDOS SQL 
"""
                              *INSECÃO NA TABELA DE TUTORES*
INSERT INTO animais_tutoratual (nome, telefone, email, motivo_doacao, data_cadastro) 
VALUES ('Carlos Silva', '(88) 99999-1234', 'carlos@email.com', 'Mudança de cidade', '2025-01-01');
INSERT INTO animais_tutoratual (nome, telefone, email, motivo_doacao, data_cadastro) 
VALUES ('João da Siva', '(88) 93799-1461', 'silva@email.com', 'Não se adaptou comigo', '2025-01-09');
                             
                             *INSECÃO NA TABELA DE ANIMAIS*
INSERT INTO animais_animal (nome, idade_em_meses, raca, descricao, sexo, tutor_id) 
VALUES ('Rex', 12, 'Labrador', 'Filhote brincalhão e amigável', 'M', 1);

                             *CONSULTA / SELECT*
SELECT a.nome AS animal_nome, a.idade_em_meses, a.raca, a.descricao, t.nome AS tutor_nome
FROM animais_animal a
LEFT JOIN animais_tutoratual t ON a.tutor_id = t.id
WHERE a.idade_em_meses > 4;

                             *ATUALIZAÇÃO / UPDATE*
UPDATE animais_animal 
SET raca = 'Golden Retriever', descricao = 'Muito dócil e perfeito para crianças'
WHERE id = 1;

                             *DELETAR / DELETE - registros da tabela TUTOR e ANIMAL*
DELETE FROM "app_animal" WHERE tutor_id = 1;
DELETE FROM "app_tutoratual" WHERE id = 1;
"""