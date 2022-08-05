from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

# Create your views here.
def logar(request):

    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():            
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'logar.html', {'user_form':user_form})


def logout_view(request):
    logout(request)
    return redirect('/')