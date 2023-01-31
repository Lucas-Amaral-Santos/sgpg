from django.shortcuts import render, redirect
from disciplina.forms import DisciplinaForm, DisciplinaOfertadaForm
from disciplina.models import Disciplina, DisciplinaOfertada
from .models import UnidadeFederativa
from .forms import UnidadeFederativaForm


def lista_tabelas(request):
    form_disciplina = DisciplinaForm()
    form_disciplina_ofertada = DisciplinaOfertadaForm()
    form_unidade_federativa = UnidadeFederativaForm()
    context = {}

    try:
        disciplina = Disciplina.objects.all()        
        context['disciplina'] = {
            'values': disciplina.values(),
            'colunas': disciplina.values()[0].keys(),
            'form': form_disciplina,
        }
    except:
        context['disciplina'] = {
            'values': None,
            'colunas': None,
            'form': form_disciplina,
        }

    try:
        disciplina_ofertada = DisciplinaOfertada.objects.all()
        context['disciplina_ofertada'] = {
            'values': disciplina_ofertada.values(),
            'colunas': disciplina_ofertada.values()[0].keys(),
            'form': form_disciplina_ofertada,
        }
    except:
        context['disciplina_ofertada'] = {
            'values': None,
            'colunas': None,
            'form': form_disciplina_ofertada,
        }

    try:
        unidade_federativa = UnidadeFederativa.objects.all()
        context['unidade_federativa'] = {
            'values': unidade_federativa.values(),
            'colunas': unidade_federativa.values()[0].keys(),
            'form': form_unidade_federativa,
        }
    except:
        context['unidade_federativa'] = {
            'values': None,
            'colunas': None,
            'form': form_unidade_federativa,
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

    if(request.method == 'POST'):
            form_unidades_federativa = UnidadeFederativaForm(request.POST)
            if(form_unidades_federativa.is_valid()):
                nova_uf = UnidadeFederativa.objects.create(
                    estado = form_unidades_federativa.cleaned_data['estado'],
                    sigla = form_unidades_federativa.cleaned_data['sigla'],
                )    
                nova_uf.save()
                return redirect('/')

    return render(request, "lista_tabelas.html", {'context': context})
