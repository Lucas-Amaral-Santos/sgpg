from django.contrib import admin
from django.urls import path

from aluno.models import Aluno
from .views import cadastra_aluno, lista_aluno, detalhes_aluno, delete_aluno

app_name = 'aluno'

urlpatterns = [
    path('cadastra/', cadastra_aluno, name='cadastra_aluno'),
    path('edita/<slug:aluno>', cadastra_aluno, name='edita_aluno'),
    path('delete/<slug:aluno>', delete_aluno, name='delete_aluno'),
    path('lista/', lista_aluno, name='lista_aluno'),
    path('<slug:aluno>', detalhes_aluno, name='detalhes_aluno'),
]
