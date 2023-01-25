from django.db import models
from professor.models import Professor

class Disciplina(models.Model):
    codigo = models.CharField(max_length=20)
    nome = models.CharField(max_length=200)
    carater = models.CharField(max_length=200)
    carga = models.IntegerField()
    creditos = models.IntegerField()
    nivel = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo+ ' - ' + self.nome

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING, related_name='disciplina_ofertada_disciplina')
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    ano = models.IntegerField()
    semestre = models.IntegerField()

    def __str__(self):
        return str(self.disciplina)

