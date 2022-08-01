from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Titulacao(models.Model):
    titulacao = models.CharField(max_length=200)
    titulacao_area = models.CharField(max_length=200)
    titulacao_ano = models.IntegerField()
    uf = models.CharField(max_length=2)
    instituicao = models.CharField(max_length=200)
    obs_geral = models.TextField()

    def __str__(self):
        return self.titulacao



class Residencia(models.Model):
    instituicao_residencia = models.CharField(max_length=200)
    residencia_ano_inicio = models.IntegerField()
    residencia_ano_fim = models.IntegerField()
    especialidade = models.CharField(max_length=200) 
    orientador = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.instituicao_residencia


class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15)

    def __str__(self):
	    return self.municipio


class Trabalho(models.Model):
    trabalho = models.CharField(max_length=200)
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING) 
    email = models.EmailField()
    data_termino = models.DateField()

    def __str__(self):
        return self.trabalho


class Graduacao(models.Model):
    graduacao_area = models.CharField(max_length=200) 
    instituicao = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    graduacao_ano_inicio = models.IntegerField()
    graduacao_ano_fim = models.IntegerField()
    residencia = models.OneToOneField(Residencia, on_delete=models.DO_NOTHING)


    def __str__(self):
	    return self.instituicao

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
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
    graduacao = models.OneToOneField(Graduacao, on_delete=models.DO_NOTHING)
    titulacao = models.OneToOneField(Titulacao, on_delete=models.DO_NOTHING)
    trabalho = models.OneToOneField(Trabalho, on_delete=models.DO_NOTHING)
    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Aluno, self).save(*args, **kwargs)


    def __str__(self):
	    return self.nome
