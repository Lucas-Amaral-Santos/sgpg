from django.contrib import admin
from .models import Evento, Participante

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    pass