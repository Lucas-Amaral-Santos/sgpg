from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Titulacao(models.Model):
    titulacao = models.CharField(max_length=200, null=True, blank=True)
    titulacao_area = models.CharField(max_length=200, null=True, blank=True)
    titulacao_ano = models.IntegerField(null=True, blank=True)
    data_qualificacao = models.DateField(null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    instituicao_titulacao = models.CharField(max_length=200, null=True, blank=True)
    obs_geral = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulacao



class Residencia(models.Model):
    instituicao_residencia = models.CharField(max_length=200, null=True, blank=True)
    residencia_ano_inicio = models.IntegerField(null=True, blank=True)
    residencia_ano_fim = models.IntegerField(null=True, blank=True)
    especialidade = models.CharField(max_length=200, null=True, blank=True) 
    uf = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.instituicao_residencia


class Endereco(models.Model):
    cep = models.CharField(max_length=8, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    municipio = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    telefone1 = models.CharField(max_length=15, null=True, blank=True)
    telefone2 = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
	    return self.municipio


class Trabalho(models.Model):
    VINCULO_CHOICES = (
        ("Estatutário", "Estatutário"),
        ("CLT", "CLT"),
        ("Autônomo", "Autônomo"),
        ("Outros", "Outros"),
    )

    trabalho = models.CharField(max_length=200, null=True, blank=True, verbose_name='Trabalho:')
    tipo_vinculo = models.CharField(max_length=200, choices=VINCULO_CHOICES, verbose_name='Tipo de Vínculo:', null=True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING, null=True, blank=True) 
    email = models.EmailField(null=True, blank=True)
    data_termino = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.trabalho


class Graduacao(models.Model):
    graduacao_area = models.CharField(max_length=200) 
    instituicao = models.CharField(max_length=200)
    local = models.CharField(max_length=200, null=True, blank=True)
    graduacao_ano_inicio = models.IntegerField(null=True, blank=True)
    graduacao_ano_fim = models.IntegerField(null=True, blank=True)
    residencia = models.OneToOneField(Residencia, on_delete=models.DO_NOTHING)


    def __str__(self):
	    return self.instituicao

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, verbose_name='CPF:')
    nome_pai = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nome do pai:')
    nome_mae = models.CharField(max_length=200, null=True, blank=True)
    naturalidade = models.CharField(max_length=2, null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)
    dt_nascimento = models.DateField()
    estado_civil = models.CharField(max_length=100, null=True, blank=True)
    identidade = models.CharField(max_length=12)
    identidade_uf = models.CharField(max_length=2)
    identidade_orgao = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    etnia = models.CharField(max_length=50, blank=True, null=True)
    situacao = models.CharField(max_length=50, null=True, blank=True)
    
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
    graduacao = models.OneToOneField(Graduacao, on_delete=models.DO_NOTHING)
    titulacao = models.OneToOneField(Titulacao, on_delete=models.DO_NOTHING)
    trabalho = models.OneToOneField(Trabalho, on_delete=models.DO_NOTHING)

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='aluno_cadastrado_por')

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Aluno, self).save(*args, **kwargs)


    def __str__(self):
	    return self.nome


class Afastamento(models.Model):
    afastamento = models.CharField(max_length=200)
    data_ini = models.DateField()
    data_fim = models.DateField()
    aluno = models.ManyToManyField(Aluno, related_name="afastamento_aluno")

    def __str__(self):
        return self.afastamento