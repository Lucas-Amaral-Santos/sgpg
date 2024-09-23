from django.contrib import admin
from .models import Colegiado

# Register your models here.
@admin.register(Colegiado)
class ColegiadoAdmin(admin.ModelAdmin):
    pass