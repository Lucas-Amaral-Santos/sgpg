from django.db import models

# Create your models here.
class UnidadeFederativa(models.Model):
    sigla = models.CharField(max_length=2)
    estado = models.CharField(max_length=50)

    def __str__(self):
            return str(self.sigla)