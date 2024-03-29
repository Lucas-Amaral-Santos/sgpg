from django.db import models
from professor.models import Professor

class Disciplina(models.Model):
    codigo = models.CharField(max_length=20)
    nome = models.CharField(max_length=200)
    carater = models.CharField(max_length=200, null=True, blank=True)
    carga = models.IntegerField()
    creditos = models.IntegerField()
    nivel = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.codigo+ ' - ' + self.nome

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING, related_name='disciplina_ofertada_disciplina', verbose_name="Disciplina")
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, verbose_name="Professor")
    ano = models.IntegerField()
    semestre = models.IntegerField()

    def __str__(self):
        return str(self.disciplina) + " - " + str(self.professor) + "(" + str(self.semestre)+ "º/" + str(self.ano) + ")"

