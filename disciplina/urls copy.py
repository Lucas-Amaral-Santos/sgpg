from django.urls import path

from .views import cadastra_disciplina

app_name = 'disciplina'

urlpatterns = [
    path('cadastra/', cadastra_disciplina, name='cadastra_disciplina'),

]
