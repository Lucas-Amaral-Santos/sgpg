from django.db import models

# Create your models here.

class Professor(models.Model):
      nome = models.CharField(max_length=200)
      sexo = models.CharField(max_length=50)
      dt_nascimento = models.DateField()
      nacionalidade = models.CharField(max_length=100)
      naturalidade = models.CharField(max_length=2)
      cpf = models.CharField(max_length=14)
      identidade = models.CharField(max_length=12)
      identidade_uf= models.CharField(max_length=2)
      identidade_orgao = models.CharField(max_length=100)
      CRM = models.CharField(max_length=100)
      Estado = models.CharField(max_length=2)
      Siape = models.CharField(max_length=30)
    
    

def __str__(self):
	    return  self.nome