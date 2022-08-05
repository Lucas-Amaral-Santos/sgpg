from django.shortcuts import redirect, render
from registrar.views import logar

def home(request):
    if (not request.user.is_authenticated):
        return redirect(logar)

    return render(request, 'home.html', {})
