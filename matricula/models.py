from django.db import models
from aluno.models import Aluno
from disciplina.models import DisciplinaOfertada
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



# Create your models here.

class Matricula(models.Model):
    numero = models.CharField(max_length=10)

    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, related_name='matricula_aluno')
    # inscricao
    # trabalho_final

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='matricula_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Matricula, self).save(*args, **kwargs)

    def __str__(self):
        return self.aluno

class Bolsa(models.Model):
    nome = models.CharField(max_length=200)
    agencia = models.CharField(max_length=200)
    dt_inicio = models.DateField()
    iniciacao_cientifica = models.BooleanField()
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING, related_name='bolsa_matricula')
    def __str__(self):
        return self.nome

class Afastamento(models.Model):
    motivo = models.CharField(max_length=200)
    saida = models.DateField()
    retorno = models.DateField()
    def __str__(self):
        return self.motivo

class Inscricao(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING, related_name='inscricao_matricula')
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.DO_NOTHING, related_name='inscricao_disciplina_ofertada')

    def __str__(self):
        return self.matricula.aluno + ' - ' + self.disciplina_ofertada