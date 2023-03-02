from django.urls import path

from .views import cadastra_afastamento, cadastra_bolsa, cadastra_inscricao, cadastra_matricula, cadastra_trabalho_final, lista_matricula, detalhe_matricula, cadastra_probatorio, lista_probatorio, detalhe_probatorio, cadastra_trabalho_probatorio, cadastra_inscricao_probatorio, detalhe_trabalho_final, gera_historico

app_name = 'matricula'

urlpatterns = [
    path('cadastra/', cadastra_matricula, name='cadastra_matricula'),
    path('cadastra_probatorio/', cadastra_probatorio, name='cadastra_probatorio'),
    path('lista_probatorio/', lista_probatorio, name='lista_probatorio'),
    path('lista_matricula/', lista_matricula, name='lista_matricula'),
    path('probatorio/<int:probatorio>/', detalhe_probatorio, name='detalhe_probatorio'),
    path('trabalho_final/<int:matricula>/', detalhe_trabalho_final, name='detalhe_trabalho_final'),
    path('<int:matricula>/', detalhe_matricula, name='detalhe_matricula'),
    path('gera_historico/<int:matricula>', gera_historico, name='gera_historico'),
    path('<int:matricula>/cadastra_bolsa', cadastra_bolsa, name='cadastra_bolsa'),
    path('<int:matricula>/cadastra_afastamento', cadastra_afastamento, name='cadastra_afastamento'),
    path('<int:matricula>/cadastra_inscricao', cadastra_inscricao, name='cadastra_inscricao'),
    path('probatorio/<int:probatorio>/cadastra_inscricao_probatorio', cadastra_inscricao_probatorio, name='cadastra_inscricao_probatorio'),
    path('<int:matricula>/cadastra_trabalho_final', cadastra_trabalho_final, name='cadastra_trabalho_final'),
    path('probatorio/<int:probatorio>/cadastra_trabalho_probatorio', cadastra_trabalho_probatorio, name='cadastra_trabalho_probatorio'),
]
