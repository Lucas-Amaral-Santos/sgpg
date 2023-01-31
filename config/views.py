from django.shortcuts import render, redirect
from disciplina.forms import DisciplinaForm, DisciplinaOfertadaForm
from disciplina.models import Disciplina, DisciplinaOfertada
from django.forms.models import model_to_dict



def lista_tabelas(request):
    disciplina = Disciplina.objects.all()
    form_disciplina = DisciplinaForm()
    print(disciplina.values())

    disciplina_ofertada = DisciplinaOfertada.objects.all()
    form_disciplina_ofertada = DisciplinaOfertadaForm()

    context = {
        'disciplina': {
            'values': disciplina.values(),
            'colunas': disciplina.values()[0].keys(),
            'form': form_disciplina,
        },
        'disciplina_ofertada': {
            'values':disciplina_ofertada.values(),
            'colunas':disciplina_ofertada.values()[0].keys(),
            'form':form_disciplina_ofertada,
        }
    }

    if(request.method == 'POST'):
        form_disciplina = DisciplinaForm(request.POST)
        if(form_disciplina.is_valid()):
            nova_disciplina = Disciplina.objects.create(
                codigo = form_disciplina.cleaned_data['codigo'],
                nome = form_disciplina.cleaned_data['nome'],
                carater = form_disciplina.cleaned_data['carater'],
                carga = form_disciplina.cleaned_data['carga'],
                creditos = form_disciplina.cleaned_data['creditos'],
                nivel = form_disciplina.cleaned_data['nivel'],
                tipo = form_disciplina.cleaned_data['tipo'],
            )    
            nova_disciplina.save()
            return redirect('/')

    if(request.method == 'POST'):
            form_disciplina_ofertada = DisciplinaOfertadaForm(request.POST)
            if(form_disciplina_ofertada.is_valid()):
                nova_inscricao = DisciplinaOfertada.objects.create(
                    disciplina = form_disciplina_ofertada.cleaned_data['disciplina'],
                    professor = form_disciplina_ofertada.cleaned_data['professor'],
                    ano = form_disciplina_ofertada.cleaned_data['ano'],
                    semestre = form_disciplina_ofertada.cleaned_data['semestre'],
                )    
                nova_inscricao.save()
                return redirect('/')

    return render(request, "lista_tabelas.html", {'context': context})

