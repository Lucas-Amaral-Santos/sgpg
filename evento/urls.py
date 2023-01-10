from django.urls import path
from .views import mostra_eventos, cadastra_evento
app_name = 'evento'

urlpatterns = [
    path('<int:mes>/<int:ano>', mostra_eventos, name='mostra_eventos'),
    path('cadastra', cadastra_evento, name='cadastra_evento')
]
