from django.db import models
from colorful.fields import RGBColorField


# Create your models here.
class UnidadeFederativa(models.Model):
    sigla = models.CharField(max_length=2)
    estado = models.CharField(max_length=50)

    def __str__(self):
            return str(self.sigla)

class Sexo(models.Model):
    sexo = models.CharField(max_length=50)
    cor = RGBColorField(default='#000000')

    def __str__(self):
            return str(self.sexo)

class Etnia(models.Model):
    etnia = models.CharField(max_length=50)
    cor = RGBColorField(default='#000000')

    def __str__(self):
            return str(self.etnia)

class EstadoCivil(models.Model):
    estado_civil = models.CharField(max_length=50)
    cor = RGBColorField(default='#000000')

    def __str__(self):
            return str(self.estado_civil)

class Vinculo(models.Model):
    vinculo = models.CharField(max_length=50)
    cor = RGBColorField(default='#000000')

    def __str__(self):
            return str(self.vinculo)
    
class StatusOptions(models.Model):
    status_options = models.CharField(max_length=50)
    cor = RGBColorField(default='#000000')

    def __str__(self):
            return str(self.status_options)
    
class LinhaPesquisa(models.Model):
    linha_pesquisa = models.CharField(max_length=200)
    cor = RGBColorField(default='#000000')

    def __str__(self):
            return str(self.linha_pesquisa)