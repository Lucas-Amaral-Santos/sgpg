from django.shortcuts import render, redirect
from disciplina.forms import DisciplinaForm, DisciplinaOfertadaForm
from disciplina.models import Disciplina, DisciplinaOfertada
from .models import UnidadeFederativa, Sexo, Etnia, EstadoCivil, Vinculo, StatusOptions, LinhaPesquisa, Instituicao, Colegio, InstituicaoResidencia, Grau
from .forms import UnidadeFederativaForm, SexoForm, EtniaForm, EstadoCivilForm, VinculoForm, StatusOptionsForm, LinhaPesquisaForm, InstituicaoForm, ColegioForm, InstituicaoResidenciaForm, GrauForm
from django.contrib import messages


def lista_tabelas(request):
    form_disciplina = DisciplinaForm()
    form_disciplina_ofertada = DisciplinaOfertadaForm()
    form_unidade_federativa = UnidadeFederativaForm()
    form_sexo = SexoForm()
    form_estado_civil = EstadoCivilForm()
    form_etnia = EtniaForm()
    form_vinculo = VinculoForm()
    form_status = StatusOptionsForm()
    form_linha_pesquisa = LinhaPesquisaForm()
    form_instituicao = InstituicaoForm()
    form_colegio = ColegioForm()
    form_instituicao_residencia = InstituicaoResidenciaForm()
    form_grau = GrauForm()

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

    try:
        status = StatusOptions.objects.all()
        context['status'] = {
            'values': status.values(),
            'colunas': status.values()[0].keys(),
            'form': form_status,
        }
    except:
        context['status'] = {
            'values': None,
            'colunas': None,
            'form': form_status,
        }

    try:
        linha_pesquisa = LinhaPesquisa.objects.all()
        context['linha_pesquisa'] = {
            'values': linha_pesquisa.values(),
            'colunas': linha_pesquisa.values()[0].keys(),
            'form': form_linha_pesquisa,
        }
    except:
        context['linha_pesquisa'] = {
            'values': None,
            'colunas': None,
            'form': form_linha_pesquisa,
        }

    try:
        instituicao = Instituicao.objects.all()
        context['instituicao'] = {
            'values': instituicao.values(),
            'colunas': instituicao.values()[0].keys(),
            'form': form_instituicao,
        }
    except:
        context['instituicao'] = {
            'values': None,
            'colunas': None,
            'form': form_instituicao,
        }

    try:
        colegio = Colegio.objects.all()
        context['colegio'] = {
            'values': colegio.values(),
            'colunas': colegio.values()[0].keys(),
            'form': form_colegio,
        }
    except:
        context['colegio'] = {
            'values': None,
            'colunas': None,
            'form': form_colegio,
        }

    try:
        colegio = Colegio.objects.all()
        context['colegio'] = {
            'values': colegio.values(),
            'colunas': colegio.values()[0].keys(),
            'form': form_colegio,
        }
    except:
        context['colegio'] = {
            'values': None,
            'colunas': None,
            'form': form_colegio,
        }

    try:
        instituicao_residencia = InstituicaoResidencia.objects.all()
        context['instituicao_residencia'] = {
            'values': instituicao_residencia.values(),
            'colunas': instituicao_residencia.values()[0].keys(),
            'form': form_instituicao_residencia,
        }
    except:
        context['instituicao_residencia'] = {
            'values': None,
            'colunas': None,
            'form': form_instituicao_residencia,
        }

    try:
        grau = Grau.objects.all()
        context['grau'] = {
            'values': grau.values(),
            'colunas': grau.values()[0].keys(),
            'form': form_grau,
        }
    except:
        context['grau'] = {
            'values': None,
            'colunas': None,
            'form': form_grau,
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
                cor = form_sexo.cleaned_data['cor'],
            )    
            nova_sexo.save()
            messages.success(request, 'Novo sexo cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_estado_civil = EstadoCivilForm(request.POST)
        if(form_estado_civil.is_valid()):
            nova_estado_civil = EstadoCivil.objects.create(
                estado_civil = form_estado_civil.cleaned_data['estado_civil'],
                cor = form_estado_civil.cleaned_data['cor'],
            )    
            nova_estado_civil.save()
            messages.success(request, 'Novo estado civil cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_etnia = EtniaForm(request.POST)
        if(form_etnia.is_valid()):
            nova_etnia = Etnia.objects.create(
                etnia = form_etnia.cleaned_data['etnia'],
                cor = form_etnia.cleaned_data['cor'],
            )    
            nova_etnia.save()
            messages.success(request, 'Nova etnia cadastrada com sucesso!')
            return redirect('config:lista_tabelas')

    if(request.method == 'POST'):
        form_vinculo = VinculoForm(request.POST)
        if(form_vinculo.is_valid()):
            nova_vinculo = Vinculo.objects.create(
                vinculo = form_vinculo.cleaned_data['vinculo'],
                cor = form_etnia.cleaned_data['cor'],
            )    
            nova_vinculo.save()
            messages.success(request, 'Novo vínculo cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_status = StatusOptionsForm(request.POST)
        if(form_status.is_valid()):
            nova_status = StatusOptions.objects.create(
                status_options = form_status.cleaned_data['status_options'],
                cor = form_status.cleaned_data['cor'],
            )    
            nova_status.save()
            messages.success(request, 'Novo status cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_linha_pesquisa = LinhaPesquisaForm(request.POST)
        if(form_linha_pesquisa.is_valid()):
            nova_linha_pesquisa = LinhaPesquisa.objects.create(
                linha_pesquisa = form_linha_pesquisa.cleaned_data['linha_pesquisa'],
                cor = form_linha_pesquisa.cleaned_data['cor'],
            )    
            nova_linha_pesquisa.save()
            messages.success(request, 'Novo linha de pesquisa cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_instituicao = InstituicaoForm(request.POST)
        if(form_instituicao.is_valid()):
            nova_instituicao = Instituicao.objects.create(
                instituicao = form_instituicao.cleaned_data['instituicao'],
                sigla = form_instituicao.cleaned_data['sigla'],
                cor = form_instituicao.cleaned_data['cor'],
            )    
            nova_instituicao.save()
            messages.success(request, 'Nova instituição cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_colegio = ColegioForm(request.POST)
        if(form_colegio.is_valid()):
            nova_colegio = Colegio.objects.create(
                colegio = form_colegio.cleaned_data['colegio'],
                sigla = form_colegio.cleaned_data['sigla'],
                cor = form_colegio.cleaned_data['cor'],
            )    
            nova_colegio.save()
            messages.success(request, 'Nova colégio cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_instituicao_residencia = InstituicaoResidenciaForm(request.POST)
        if(form_instituicao_residencia.is_valid()):
            nova_instituicao_residencia = InstituicaoResidencia.objects.create(
                instituicao_residencia = form_instituicao_residencia.cleaned_data['instituicao_residencia'],
                cor = form_instituicao_residencia.cleaned_data['cor'],
            )    
            nova_instituicao_residencia.save()
            messages.success(request, 'Nova instituição de residência cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_grau = GrauForm(request.POST)
        if(form_grau.is_valid()):
            novo_grau = Grau.objects.create(
                grau = form_grau.cleaned_data['grau'],
                cor = form_grau.cleaned_data['cor'],
            )    
            novo_grau.save()
            messages.success(request, 'Nova grau cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    return render(request, "lista_tabelas.html", {'context': context})
