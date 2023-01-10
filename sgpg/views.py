from datetime import datetime
from django.shortcuts import redirect, render
from registrar.views import logar

def home(request):
    if (not request.user.is_authenticated):
        return redirect(logar)

    data = datetime.today

    return render(request, 'home.html', {'data': data})
