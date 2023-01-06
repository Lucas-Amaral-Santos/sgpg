from django.shortcuts import render, redirect
from .forms import DisciplinaForm, DisciplinaOfertada, DisciplinaOfertadaForm
from .models import Disciplina, DisciplinaOfertada
# Create your views here.
def cadastra_disciplina(request):
    form = DisciplinaForm()

    if(request.method == 'POST'):
        form = DisciplinaForm(request.POST)
        if(form.is_valid()):
            nova_disciplina = Disciplina.objects.create(
                codigo = form.cleaned_data['codigo'],
                nome = form.cleaned_data['nome'],
                carater = form.cleaned_data['carater'],
                carga = form.cleaned_data['carga'],
                creditos = form.cleaned_data['creditos'],
                nivel = form.cleaned_data['nivel'],
                tipo = form.cleaned_data['tipo'],
            )    
            nova_disciplina.save()
            return redirect('/')

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina': 'Cadastra Disciplina'})

def cadastra_disciplina_ofertada(request):
    form = DisciplinaOfertadaForm()

    if(request.method == 'POST'):
        form = DisciplinaOfertadaForm(request.POST)
        if(form.is_valid()):
            nova_inscricao = DisciplinaOfertada.objects.create(
                disciplina = form.cleaned_data['disciplina'],
                professor = form.cleaned_data['professor'],
                ano = form.cleaned_data['ano'],
                semestre = form.cleaned_data['semestre'],
            )    
            nova_inscricao.save()
            return redirect('/')

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina': 'Cadastra Disciplina Ofertada'})