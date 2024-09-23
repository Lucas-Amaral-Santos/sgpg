from django.db import models
from matricula.models import Matricula
from professor.models import Professor

# Create your models here.
class Colegiado(models.Model):

    STATUS_COLEGIADO_CHOICES = (
        ("Titular", "Titular"),
        ("Suplente", "Suplente"),
    )
    colegiado_data_entrada = models.DateField()
    colegiado_data_saida = models.DateField(null=True, blank=True)
    status_membro = models.CharField(max_length=100, choices=STATUS_COLEGIADO_CHOICES, verbose_name='Status:')
    matricula_membro = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING, null=True)
    professor_membro = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        if self.colegiado_data_saida:
                return 'Não Membro'
        else:
                return 'Membro'