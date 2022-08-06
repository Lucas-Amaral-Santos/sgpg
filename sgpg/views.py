from datetime import datetime

from django.shortcuts import redirect, render
from registrar.views import logar

def home(request):
    if (not request.user.is_authenticated):
        return redirect(logar)

    ano = datetime.today().year

    return render(request, 'home.html', {'ano': ano})
