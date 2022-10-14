from django.urls import path

from .views import cadastra_matricula, lista_matricula, detalhe_matricula, cadastra_probatorio, lista_probatorio

app_name = 'matricula'

urlpatterns = [
    path('cadastra/', cadastra_matricula, name='cadastra_matricula'),
    path('cadastra_probatorio/', cadastra_probatorio, name='cadastra_probatorio'),
    path('lista_probatorio/', lista_probatorio, name='lista_probatorio'),
    path('lista_matricula/', lista_matricula, name='lista_matricula'),
    path('<slug:matricula>/', detalhe_matricula, name='detalhe_matricula'
    ),
]
