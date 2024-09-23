
from django.contrib import admin
from django.urls import path
from .views import detalhes_colegiado

app_name = 'colegiado'

urlpatterns = [
    path('', detalhes_colegiado, name='detalhes_colegiado')
]
