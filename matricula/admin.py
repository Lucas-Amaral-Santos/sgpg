from django.contrib import admin

from .models import Matricula, Inscricao, Probatorio, TrabalhoFinal, VersaoFinal, Nota, ExameLinguas

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

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    pass

@admin.register(VersaoFinal)
class VersaoFinalAdmin(admin.ModelAdmin):
    pass

@admin.register(ExameLinguas)
class ExameLinguasAdmin(admin.ModelAdmin):
    pass