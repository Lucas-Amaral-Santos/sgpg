from django.urls import path

from .views import lista_tabelas

app_name = 'config'

urlpatterns = [
    path('lista_tabelas/', lista_tabelas, name='lista_tabelas'),

]
