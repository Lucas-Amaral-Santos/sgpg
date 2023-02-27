from django.contrib import admin
from .models import UnidadeFederativa, Sexo, EstadoCivil, Etnia

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