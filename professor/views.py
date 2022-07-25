from django.shortcuts import render
from .forms import ProfForm
from  .models import Professor

# Create your views here.

def cadastra_professor(request):
    form = ProfForm
    if request.method == "POST":
        form = ProfForm(request.POST)
        if form.is_valid():
            novo_professor = Professor.objects.create(
                nome = form.cleaned_data['nome'],
                sexo = form.cleaned_data['sexo'],
                dt_nascimento = form.cleaned_data['dt_nascimento'],
                nacionalidade = form.cleaned_data['nacionalidade'],
                naturalidade = form.cleaned_data['naturalidade'],
                cpf = form.cleaned_data['cpf'],
                identidade = form.cleaned_data['identidade'], 
                identidade_orgao = form.cleaned_data['identidade_orgao'],
                CRM = form.cleaned_data['CRM'],
                estado = form.cleaned_data['estado'],
                Siape= form.cleaned_data['Siape'],
                
               
            )
        novo_professor.save()


    return render(request, "cadastra_professor.html", {'form':form})