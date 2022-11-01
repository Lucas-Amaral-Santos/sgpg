from django.contrib import admin
from .models import Aluno, Endereco, Graduacao

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass


@admin.register(Graduacao)
class GraduacaoAdmin(admin.ModelAdmin):
    pass