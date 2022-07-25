from django.contrib import admin
from django.urls import path
from .views import cadastra_professor

urlpatterns = [
    path('cadastra/', cadastra_professor, name='cadastra_professor'),
]