from django.contrib import admin
from .models import UnidadeFederativa, Sexo

# Register your models here.
@admin.register(UnidadeFederativa)
class UnidadeFederativaAdmin(admin.ModelAdmin):
    pass


@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    pass
