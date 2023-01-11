from django.contrib import admin

from .models import Matricula, Inscricao, Probatorio, TrabalhoFinal

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

@admin.register(TrabalhoFinal)
class TrabalhoFinalAdmin(admin.ModelAdmin):
    pass