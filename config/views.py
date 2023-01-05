from django.shortcuts import render

# Create your views here.
def lista_tabelas(request):

    return render(request, "lista_tabelas.html")