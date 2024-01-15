from django.contrib import admin
from .models import UnidadeFederativa, Sexo, EstadoCivil, Etnia, StatusOptions, LinhaPesquisa, Instituicao, Colegio, Grau, Linguas

# Register your models here.
@admin.register(UnidadeFederativa)
class UnidadeFederativaAdmin(admin.ModelAdmin):
    pass

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    pass

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    pass

@admin.register(Etnia)
class EtniaAdmin(admin.ModelAdmin):
    pass

@admin.register(StatusOptions)
class StatusOptionsAdmin(admin.ModelAdmin):
    pass

@admin.register(LinhaPesquisa)
class LinhaPesquisaAdmin(admin.ModelAdmin):
    pass

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    pass

@admin.register(Linguas)
class LinguasAdmin(admin.ModelAdmin):
    pass

