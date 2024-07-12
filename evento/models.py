from django.db import models
from professor.models import Professor
from matricula.models import TrabalhoFinal
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Evento(models.Model):
    evento_tipo_choices = (
         ('Qualificação','Qualificação'),
         ('Defesa de Dissertação','Defesa de Dissertação'),
         ('Defesa de Tese', 'Defesa de Tese'),
         ('Seminários', 'Seminários'),
         ('Palestras', 'Palestras'),
         ('Encontros', 'Encontros'),
    ) 
    evento = models.CharField(max_length=200, verbose_name="Nome do evento:")
    evento_data = models.DateField(verbose_name="Data do evento:")
    evento_hora = models.TimeField(verbose_name="Hora:")
    evento_trabalho_final = models.ForeignKey(TrabalhoFinal, null=True, blank=True, on_delete=models.CASCADE, related_name='evento_trabalho_final', verbose_name="Trabalho final:")
    evento_tipo = models.CharField(max_length=200, choices=evento_tipo_choices, verbose_name='Tipo: ')
    evento_obs = models.TextField(null=True, blank=True)

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='evento_cadastrado_por')

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.evento)

class Convidados(models.Model):
    TIPO_CONVIDADO_CHOICES = (
        ('Palestrante','Palestrante'),
        ('Organizador','Organizador'),
    )
    convidado = models.CharField(max_length=200)
    convidado_tipo = models.CharField(max_length=20, choices=TIPO_CONVIDADO_CHOICES)

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='convidados_evento')

    def __str__(self):
        return str(self.convidado)


class Participante(models.Model):
    TIPO_PARTICIPANTE_CHOICES = (
        ('Orientador','Orientador'),
        ('Coorientador','Coorientador'),
        ('Banca','Banca'),
    )

    participante_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='participante_professor')
    participante_tipo = models.CharField(max_length=20, choices=TIPO_PARTICIPANTE_CHOICES)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes_evento')


    def __str__(self):
        return str(self.participante_professor)
