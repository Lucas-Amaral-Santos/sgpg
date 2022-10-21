from email.policy import default
from django.db import models
from aluno.models import Aluno
from disciplina.models import DisciplinaOfertada
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class Curso(models.Model):

    CURSO_CHOICES = (
        ("Mestrado", "Mestrado"),
        ("Doutorado", "Doutorado"),
    )
    curso = models.CharField(max_length=200, choices=CURSO_CHOICES)
    orientador = models.CharField(max_length=200)
    coorientador = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Curso, self).save(*args, **kwargs)

# Create your models here.
class Probatorio(models.Model):
    data_inscricao = models.DateField()
    nota = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, related_name='probatorio_aluno')

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='probatorio_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Probatorio, self).save(*args, **kwargs)

    def __str__(self):
        return self.aluno.nome

class Matricula(models.Model):
    numero = models.CharField(max_length=10)

    probatorio = models.ForeignKey(Probatorio, on_delete=models.DO_NOTHING, related_name='matricula_probatorio')

    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, related_name="matricula_curso", null=True, blank=True)
    status = models.CharField(max_length=50, default='Matriculado')
    requisita_bolsa = models.BooleanField()
    # trabalho_final

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='matricula_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Matricula, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.probatorio.aluno)


class Bolsa(models.Model):
    nome = models.CharField(max_length=200)
    agencia = models.CharField(max_length=200)
    dt_inicio = models.DateField()
    iniciacao_cientifica = models.BooleanField()
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING, related_name='bolsa_matricula')
    dt_cadastro = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome

class Afastamento(models.Model):
    motivo = models.CharField(max_length=200)
    saida = models.DateField()
    retorno = models.DateField()
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING, related_name='afastamento_matricula')

    dt_cadastro = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.motivo


class Inscricao(models.Model):

    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.DO_NOTHING, related_name='inscricao_disciplina_ofertada')
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING, related_name="inscricao_matricula")
    nota = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)])

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='inscricao_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Inscricao, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.disciplina_ofertada)