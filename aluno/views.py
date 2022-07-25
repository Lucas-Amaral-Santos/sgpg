from django.shortcuts import render
from .forms import AlunoForm
from .models import Aluno
# Create your views here.

def cadastra_aluno(request):
    form = AlunoForm
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            novo_aluno = Aluno.objects.create(
                nome = form.cleaned_data['nome'],
                cpf = form.cleaned_data['cpf'],
                nome_pai = form.cleaned_data['nome_pai'],
                nome_mae = form.cleaned_data['nome_mae'],
                naturalidade = form.cleaned_data['naturalidade'],
                nacionalidade = form.cleaned_data['nacionalidade'],
                dt_nascimento = form.cleaned_data['dt_nascimento'],
                estado_civil = form.cleaned_data['estado_civil'],
                identidade = form.cleaned_data['identidade'],
                identidade_uf = form.cleaned_data['identidade_uf'],
                identidade_orgao = form.cleaned_data['identidade_orgao'],
                sexo = form.cleaned_data['sexo'],
                email = form.cleaned_data['email']
            )
            novo_aluno.save()

    return render(request, "cadastra_aluno.html", {'form':form})

def lista_aluno(request):
    alunos = Aluno.objects.all().order_by('nome')

    return render(request, 'pesquisaaluno.html' , {'alunos': alunos})


