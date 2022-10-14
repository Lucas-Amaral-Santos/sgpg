from django.contrib import admin

from .models import Matricula, Inscricao

# Register your models here.
@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    pass


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    pass