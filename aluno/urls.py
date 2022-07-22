from django.contrib import admin
from django.urls import path
from .views import cadastra_aluno
urlpatterns = [
    path('cadastra/', cadastra_aluno, name='cadastra_aluno'),
]
