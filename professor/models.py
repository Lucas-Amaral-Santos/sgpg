from django.db import models
from aluno.models import Endereco, Titulacao, Graduacao
from django.contrib.auth.models import User
# Create your models here.

class PosDoutorado(models.Model):
      concluido = models.BooleanField()
      ano_inicio = models.IntegerField()
      ano_fim = models.IntegerField()
      instituicao = models.CharField(max_length=200)
      pais = models.CharField(max_length=200)

class Trabalho(models.Model):
      instituicao = models.CharField(max_length=200)
      setor = models.CharField(max_length=200)
      admissao = models .DateField()
      cargo = models.CharField(max_length=200)
      telefone  = models.CharField(max_length=15)
      categoria = models.CharField(max_length=200) 
      email = models.EmailField()

      def __str__(self):
            return self.instituicao


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
      tipo_trab = models.CharField(max_length=100)
      endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
      titulacao = models.OneToOneField(Titulacao, on_delete=models.DO_NOTHING)
      graduacao = models.OneToOneField(Graduacao, on_delete=models.DO_NOTHING, null=True)
      trabalho = models.ForeignKey(Trabalho, on_delete=models.DO_NOTHING, related_name="professor_trabalho")
      pos_doutorado = models.ForeignKey(PosDoutorado, on_delete=models.DO_NOTHING, related_name="professor_pos_doutorado")

      slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
      updated = models.DateTimeField(auto_now=True)
      cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='professor_cadastrado_por')

      def __str__(self):
            return  self.nome