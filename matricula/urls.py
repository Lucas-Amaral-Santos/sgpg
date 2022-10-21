from django.urls import path

from .views import cadastra_afastamento, cadastra_bolsa, cadastra_inscricao, cadastra_matricula, lista_matricula, detalhe_matricula, cadastra_probatorio, lista_probatorio

app_name = 'matricula'

urlpatterns = [
    path('cadastra/', cadastra_matricula, name='cadastra_matricula'),
    path('cadastra_probatorio/', cadastra_probatorio, name='cadastra_probatorio'),
    path('lista_probatorio/', lista_probatorio, name='lista_probatorio'),
    path('lista_matricula/', lista_matricula, name='lista_matricula'),
    path('<slug:matricula>/', detalhe_matricula, name='detalhe_matricula'),
    path('<slug:matricula>/cadastra_bolsa', cadastra_bolsa, name='cadastra_bolsa'),
    path('<slug:matricula>/cadastra_afastamento', cadastra_afastamento, name='cadastra_afastamento'),
    path('<slug:matricula>/cadastra_inscricao', cadastra_inscricao, name='cadastra_inscricao'),
]
