from django.contrib import admin

from .models import Matricula

# Register your models here.
@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    pass