from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    nome_pai = models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)
    naturalidade = models.CharField(max_length=2)
    nacionalidade = models.CharField(max_length=100)
    dt_nascimento = models.DateField()
    estado_civil = models.CharField(max_length=100)
    identidade = models.CharField(max_length=12)
    identidade_uf = models.CharField(max_length=2)
    identidade_orgao = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
	    return self.nome
