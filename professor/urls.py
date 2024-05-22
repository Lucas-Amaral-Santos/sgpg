from django.contrib import admin
from django.urls import path
from .views import cadastra_professor, lista_professor, detalhes_colegiado, detalhes_professor, delete_professor, edita_colegiado

app_name = 'professor'

urlpatterns = [
    path('cadastra/', cadastra_professor, name='cadastra_professor'),
    path('edita/<slug:professor>', cadastra_professor, name='edita_professor'),
    path('lista/', lista_professor, name='lista_professor'),
    path('<int:professor>/', detalhes_professor, name='detalhes_professor'),
    path('colegiado/', detalhes_colegiado, name='detalhes_colegiado'),
    path('edita_colegiado/<int:colegiado>', edita_colegiado, name='edita_colegiado'),
    path('delete/<slug:professor>', delete_professor, name='delete_professor'),
]