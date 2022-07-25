from django.contrib import admin
from django.urls import path

from aluno.models import Aluno
from .views import cadastra_aluno, lista_aluno
urlpatterns = [
    path('cadastra/', cadastra_aluno, name='cadastra_aluno'),
    path('lista/', lista_aluno, name = 'lista_aluno')

]
