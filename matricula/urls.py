from django.urls import path

from .views import cadastra_matricula, lista_matricula, detalhe_matricula

app_name = 'matricula'

urlpatterns = [
    path('cadastra/', cadastra_matricula, name='cadastra_matricula'),
    path('lista_matricula/', lista_matricula, name='lista_matricula'),
    path('<slug:matricula>/', detalhe_matricula, name='detalhe_matricula'
    ),
]
