from django.contrib import admin
from django.urls import path
from .views import cadastra_professor, lista_professor

app_name = 'professor'

urlpatterns = [
    path('cadastra/', cadastra_professor, name='cadastra_professor'),
    path('lista/', lista_professor, name='lista_professor')
]