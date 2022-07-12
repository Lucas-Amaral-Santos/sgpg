from django.shortcuts import render
from datetime import datetime


def home(request):
    ano = datetime.today().year
    return render(request, 'home.html', {'ano': ano})
