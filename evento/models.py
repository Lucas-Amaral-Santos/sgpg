from django.db import models
from professor.models import Professor
from matricula.models import TrabalhoFinal
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Evento(models.Model):
    evento = models.CharField(max_length=200)
    evento_data = models.DateField()
    evento_hora = models.TimeField()
    evento_trabalho_final = models.OneToOneField(TrabalhoFinal, on_delete=models.CASCADE, related_name='evento_trabalho_final')

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='evento_cadastrado_por')

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.evento)

class Participante(models.Model):
    TIPO_PARTICIPANTE_CHOICES = (
        ('Orientador','Orientador'),
        ('Coorientador','Coorientador'),
        ('Banca','Banca'),
    )

    participante_professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, related_name='participante_professor')
    participante_tipo = models.CharField(max_length=20, choices=TIPO_PARTICIPANTE_CHOICES)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING, related_name='participantes_evento')


    def __str__(self):
        return str(self.participante_professor)
