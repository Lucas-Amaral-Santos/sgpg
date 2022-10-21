from django.urls import path

from .views import cadastra_disciplina, cadastra_disciplina_ofertada

app_name = 'disciplina'

urlpatterns = [
    path('cadastra_disciplina/', cadastra_disciplina, name='cadastra_disciplina'),
    path('cadastra_disciplina_ofertada/', cadastra_disciplina_ofertada, name='cadastra_disciplina_ofertada'),

]
