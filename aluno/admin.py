from django.contrib import admin
from .models import Aluno

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass