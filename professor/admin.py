from django.contrib import admin
from .models import Professor, PosDoutorado, Trabalho

# Register your models here.
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass


@admin.register(PosDoutorado)
class PosDoutoradoAdmin(admin.ModelAdmin):
    pass

@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    pass