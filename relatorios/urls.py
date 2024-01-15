from django.contrib import admin
from django.urls import path
from .views import filtra_aluno

app_name = 'relatorios'

urlpatterns = [
    path('aluno/', filtra_aluno, name="filtra_aluno"),


]
