from django.urls import path

from .views import cadastra_disciplina, cadastra_inscricao

app_name = 'disciplina'

urlpatterns = [
    path('cadastra_disciplina/', cadastra_disciplina, name='cadastra_disciplina'),
    path('cadastra_inscricao/', cadastra_inscricao, name='cadastra_inscricao'),

]
