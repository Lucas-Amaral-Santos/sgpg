from django.contrib import admin
from django.urls import path
from .views import cadastra_professor, lista_professor, detalhes_colegiado, detalhes_professor

app_name = 'professor'

urlpatterns = [
    path('cadastra/', cadastra_professor, name='cadastra_professor'),
    path('lista/', lista_professor, name='lista_professor'),
    path('<int:professor>/', detalhes_professor, name='detalhes_professor'),
    path('colegiado/', detalhes_colegiado, name='detalhes_colegiado'),
]