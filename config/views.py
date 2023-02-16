from django.shortcuts import render, redirect
from disciplina.forms import DisciplinaForm, DisciplinaOfertadaForm
from disciplina.models import Disciplina, DisciplinaOfertada
from .models import UnidadeFederativa, Sexo, Etnia, EstadoCivil, Vinculo
from .forms import UnidadeFederativaForm, SexoForm, EtniaForm, EstadoCivilForm, VinculoForm
from django.contrib import messages


def lista_tabelas(request):
    form_disciplina = DisciplinaForm()
    form_disciplina_ofertada = DisciplinaOfertadaForm()
    form_unidade_federativa = UnidadeFederativaForm()
    form_sexo = SexoForm()
    form_estado_civil = EstadoCivilForm()
    form_etnia = EtniaForm()
    form_vinculo = VinculoForm()

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

    try:
        sexo = Sexo.objects.all()
        context['sexo'] = {
            'values': sexo.values(),
            'colunas': sexo.values()[0].keys(),
            'form': form_sexo,
        }
    except:
        context['sexo'] = {
            'values': None,
            'colunas': None,
            'form': form_sexo,
        }

    try:
        etnia = Etnia.objects.all()
        context['etnia'] = {
            'values': etnia.values(),
            'colunas': etnia.values()[0].keys(),
            'form': form_etnia,
        }
    except:
        context['etnia'] = {
            'values': None,
            'colunas': None,
            'form': form_etnia,
        }

    try:
        estado_civil = EstadoCivil.objects.all()
        context['estado_civil'] = {
            'values': estado_civil.values(),
            'colunas': estado_civil.values()[0].keys(),
            'form': form_estado_civil,
        }
    except:
        context['estado_civil'] = {
            'values': None,
            'colunas': None,
            'form': form_estado_civil,
        }


    try:
        vinculo = Vinculo.objects.all()
        context['vinculo'] = {
            'values': vinculo.values(),
            'colunas': vinculo.values()[0].keys(),
            'form': form_vinculo,
        }
    except:
        context['vinculo'] = {
            'values': None,
            'colunas': None,
            'form': form_vinculo,
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
            messages.success(request, 'Nova disciplina cadastrada com sucesso!')
            return redirect('config:lista_tabelas')

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
            messages.success(request, 'Nova disciplina ofertada cadastrada com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_unidades_federativa = UnidadeFederativaForm(request.POST)
        if(form_unidades_federativa.is_valid()):
            nova_uf = UnidadeFederativa.objects.create(
                estado = form_unidades_federativa.cleaned_data['estado'],
                sigla = form_unidades_federativa.cleaned_data['sigla'],
            )    
            nova_uf.save()
            messages.success(request, 'Novo UF cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_sexo = SexoForm(request.POST)
        if(form_sexo.is_valid()):
            nova_sexo = Sexo.objects.create(
                sexo = form_sexo.cleaned_data['sexo'],
            )    
            nova_sexo.save()
            messages.success(request, 'Novo sexo cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_estado_civil = EstadoCivilForm(request.POST)
        if(form_estado_civil.is_valid()):
            nova_estado_civil = EstadoCivil.objects.create(
                estado_civil = form_estado_civil.cleaned_data['estado_civil'],
            )    
            nova_estado_civil.save()
            messages.success(request, 'Novo estado civil cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_etnia = EtniaForm(request.POST)
        if(form_etnia.is_valid()):
            nova_etnia = Etnia.objects.create(
                etnia = form_etnia.cleaned_data['etnia'],
            )    
            nova_etnia.save()
            messages.success(request, 'Nova etnia cadastrada com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_vinculo = VinculoForm(request.POST)
        if(form_vinculo.is_valid()):
            nova_vinculo = Vinculo.objects.create(
                vinculo = form_vinculo.cleaned_data['vinculo'],
            )    
            nova_vinculo.save()
            messages.success(request, 'Novo vínculo cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    return render(request, "lista_tabelas.html", {'context': context})
