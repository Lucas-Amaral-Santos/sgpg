from django.contrib import admin

from .models import Matricula, Inscricao, Probatorio

# Register your models here.
@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    pass


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Probatorio)
class ProbatorioAdmin(admin.ModelAdmin):
    pass