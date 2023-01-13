from django.urls import path
from .views import mostra_eventos, cadastra_evento, cadastra_participante, detalhes_evento
app_name = 'evento'

urlpatterns = [
    path('', mostra_eventos, name='mostra_eventos_sem_slug'),
    path('<int:mes>/<int:ano>', mostra_eventos, name='mostra_eventos'),
    path('detalhes_evento/<int:evento>', detalhes_evento, name='detalhes_evento'),
    path('cadastra', cadastra_evento, name='cadastra_evento'),
    path('cadastra/<str:data>', cadastra_evento, name='cadastra_evento_data'),
    path('cadastra_participante/<int:evento>', cadastra_participante, name='cadastra_participante')
]
