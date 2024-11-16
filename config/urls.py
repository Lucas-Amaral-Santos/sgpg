from django.urls import path

from .views import lista_tabelas, delete_object, edit_object

app_name = 'config'

urlpatterns = [
    path('lista_tabelas/', lista_tabelas, name='lista_tabelas'),
    path('delete/<str:tabela>/<int:id>', delete_object, name='delete_object'),
    path('edit/<str:tabela>/<int:id>', edit_object, name='edit_object'),

]
