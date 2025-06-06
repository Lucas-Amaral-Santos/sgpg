from django.shortcuts import render, redirect
from disciplina.forms import DisciplinaForm, DisciplinaOfertadaForm
from disciplina.models import Disciplina, DisciplinaOfertada
from .models import UnidadeFederativa, Sexo, Etnia, EstadoCivil, Vinculo, \
                    StatusOptions, LinhaPesquisa, Instituicao, Colegio, \
                    InstituicaoResidencia, Grau, Linguas, AgenciaFomento
from .forms import UnidadeFederativaForm, SexoForm, EtniaForm, EstadoCivilForm, \
                    VinculoForm, StatusOptionsForm, LinhaPesquisaForm, InstituicaoForm, \
                    ColegioForm, InstituicaoResidenciaForm, GrauForm, LinguasForm, AgenciaFomentoForm
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
    form_linguas = LinguasForm()
    form_agencia_fomento = AgenciaFomentoForm()

    context = {}

    try:
        disciplina = Disciplina.objects.all()        
        context['disciplina'] = {
            'values': disciplina.values(),
            'colunas': disciplina.values()[0].keys(),
            'form': form_disciplina,
            'titulo': 'Disciplina',
            'tabela': 'disciplina'
        }
    except:
        context['disciplina'] = {
            'values': None,
            'colunas': None,
            'form': form_disciplina,
            'titulo': 'Disciplina',
            'tabela': 'disciplina'
        }

    try:
        disciplina_ofertada = DisciplinaOfertada.objects.all()
        context['disciplina_ofertada'] = {
            'values': disciplina_ofertada.values(),
            'colunas': disciplina_ofertada.values()[0].keys(),
            'form': form_disciplina_ofertada,
            'titulo': 'Disciplina Ofertada',
            'tabela': 'disciplina_ofertada'
        }
    except:
        context['disciplina_ofertada'] = {
            'values': None,
            'colunas': None,
            'form': form_disciplina_ofertada,
            'titulo': 'Disciplina Ofertada',
            'tabela': 'disciplina_ofertada'
        }

    try:
        unidade_federativa = UnidadeFederativa.objects.all()
        context['unidade_federativa'] = {
            'values': unidade_federativa.values(),
            'colunas': unidade_federativa.values()[0].keys(),
            'form': form_unidade_federativa,
            'titulo': 'Unidade Federativa',
            'tabela': 'unidade_federativa'
        }
    except:
        context['unidade_federativa'] = {
            'values': None,
            'colunas': None,
            'form': form_unidade_federativa,
            'titulo': 'Unidade Federativa',
            'tabela': 'unidade_federativa'
        }

    try:
        sexo = Sexo.objects.all()
        context['sexo'] = {
            'values': sexo.values(),
            'colunas': sexo.values()[0].keys(),
            'form': form_sexo,
            'titulo': 'Sexo',
            'tabela': 'sexo'
        }
    except:
        context['sexo'] = {
            'values': None,
            'colunas': None,
            'form': form_sexo,
            'titulo': 'Sexo',
            'tabela': 'sexo'
        }

    try:
        etnia = Etnia.objects.all()
        context['etnia'] = {
            'values': etnia.values(),
            'colunas': etnia.values()[0].keys(),
            'form': form_etnia,
            'titulo': 'Raça/Etnia',
            'tabela': 'etnia'
        }
    except:
        context['etnia'] = {
            'values': None,
            'colunas': None,
            'form': form_etnia,
            'titulo': 'Raça/Etnia',
            'tabela': 'etnia'
        }

    try:
        estado_civil = EstadoCivil.objects.all()
        context['estado_civil'] = {
            'values': estado_civil.values(),
            'colunas': estado_civil.values()[0].keys(),
            'form': form_estado_civil,
            'titulo': 'Estado Civil',
            'tabela': 'estado_civil'
        }
    except:
        context['estado_civil'] = {
            'values': None,
            'colunas': None,
            'form': form_estado_civil,
            'titulo': 'Estado Civil',
            'tabela': 'estado_civil'
        }


    try:
        vinculo = Vinculo.objects.all()
        context['vinculo'] = {
            'values': vinculo.values(),
            'colunas': vinculo.values()[0].keys(),
            'form': form_vinculo,
            'titulo': 'Vínculo',
            'tabela': 'vinculo'
        }
    except:
        context['vinculo'] = {
            'values': None,
            'colunas': None,
            'form': form_vinculo,
            'titulo': 'Vínculo',
            'tabela': 'vinculo'
        }

    try:
        status = StatusOptions.objects.all()
        context['status'] = {
            'values': status.values(),
            'colunas': status.values()[0].keys(),
            'form': form_status,
            'titulo': 'Status',
            'tabela': 'status'
        }
    except:
        context['status'] = {
            'values': None,
            'colunas': None,
            'form': form_status,
            'titulo': 'Status',
            'tabela': 'status'
        }

    try:
        linha_pesquisa = LinhaPesquisa.objects.all()
        context['linha_pesquisa'] = {
            'values': linha_pesquisa.values(),
            'colunas': linha_pesquisa.values()[0].keys(),
            'form': form_linha_pesquisa,
            'titulo': 'Linha de Pesquisa',
            'tabela': 'linha_pesquisa'
        }
    except:
        context['linha_pesquisa'] = {
            'values': None,
            'colunas': None,
            'form': form_linha_pesquisa,
            'titulo': 'Linha de Pesquisa',
            'tabela': 'linha_pesquisa'
        }

    try:
        instituicao = Instituicao.objects.all()
        context['instituicao'] = {
            'values': instituicao.values(),
            'colunas': instituicao.values()[0].keys(),
            'form': form_instituicao,
            'titulo': 'Instituição',
            'tabela': 'instituicao'
            
        }
    except:
        context['instituicao'] = {
            'values': None,
            'colunas': None,
            'form': form_instituicao,
            'titulo': 'Instituição',
            'tabela': 'instituicao'
        }

    try:
        colegio = Colegio.objects.all()
        context['colegio'] = {
            'values': colegio.values(),
            'colunas': colegio.values()[0].keys(),
            'form': form_colegio,
            'titulo': 'Colégio',
            'tabela': 'colegio'
        }
    except:
        context['colegio'] = {
            'values': None,
            'colunas': None,
            'form': form_colegio,
            'titulo': 'Colégio',
            'tabela': 'colegio'
        }

    try:
        instituicao_residencia = InstituicaoResidencia.objects.all()
        context['instituicao_residencia'] = {
            'values': instituicao_residencia.values(),
            'colunas': instituicao_residencia.values()[0].keys(),
            'form': form_instituicao_residencia,
            'titulo': 'Instuição de Residência',
            'tabela': 'instituicao_residencia'
        }
    except:
        context['instituicao_residencia'] = {
            'values': None,
            'colunas': None,
            'form': form_instituicao_residencia,
            'titulo': 'Instuição de Residência',
            'tabela': 'instituicao_residencia'
        }

    try:
        grau = Grau.objects.all()
        context['grau'] = {
            'values': grau.values(),
            'colunas': grau.values()[0].keys(),
            'form': form_grau,
            'titulo': 'Grau',
            'tabela': 'grau'
        }
    except:
        context['grau'] = {
            'values': None,
            'colunas': None,
            'form': form_grau,
            'titulo': 'Grau',
            'tabela': 'grau'
        }

    try:
        linguas = Linguas.objects.all()
        context['linguas'] = {
            'values': linguas.values(),
            'colunas': linguas.values()[0].keys(),
            'form': form_linguas,
            'titulo': 'Linguas',
            'tabela': 'linguas'
        }
    except:
        context['linguas'] = {
            'values': None,
            'colunas': None,
            'form': form_linguas,
            'titulo': 'Linguas',
            'tabela': 'linguas'
        }

    try:
        agencia_fomento = AgenciaFomento.objects.all()
        context['agencia_fomento'] = {
            'values': agencia_fomento.values(),
            'colunas': agencia_fomento.values()[0].keys(),
            'form': form_agencia_fomento,
            'titulo': 'Agência de Fomento',
            'tabela': 'agencia_fomento'
        }
    except:
        context['agencia_fomento'] = {
            'values': None,
            'colunas': None,
            'form': form_agencia_fomento,
            'titulo': 'Agência de Fomento',
            'tabela': 'agencia_fomento'
        }

    if(request.method == 'POST'):
        form_disciplina = DisciplinaForm(request.POST)
        if(form_disciplina.is_valid()):
            nova_disciplina = Disciplina.objects.create(
                codigo = form_disciplina.cleaned_data['codigo'],
                nome = form_disciplina.cleaned_data['nome'],
                # carater = form_disciplina.cleaned_data['carater'],
                carga = form_disciplina.cleaned_data['carga'],
                creditos = form_disciplina.cleaned_data['creditos'],
                # nivel = form_disciplina.cleaned_data['nivel'],
                # tipo = form_disciplina.cleaned_data['tipo'],
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
    
    if(request.method == 'POST'):
        form_linguas = LinguasForm(request.POST)
        if(form_linguas.is_valid()):
            novo_linguas = Linguas.objects.create(
                lingua = form_linguas.cleaned_data['lingua'],
                cor = form_linguas.cleaned_data['cor'],
            )    
            novo_linguas.save()
            messages.success(request, 'Nova lingua cadastrado com sucesso!')
            return redirect('config:lista_tabelas')
        
    if(request.method == 'POST'):
        form_agencia_fomento = AgenciaFomentoForm(request.POST)
        if(form_agencia_fomento.is_valid()):
            novo_agencia_fomento = AgenciaFomento.objects.create(
                agencia_fomento = form_agencia_fomento.cleaned_data['agencia_fomento'],
                cor = form_agencia_fomento.cleaned_data['cor'],
            )    
            novo_agencia_fomento.save()
            messages.success(request, 'Nova agência de fomento cadastrado com sucesso!')
            return redirect('config:lista_tabelas')

    return render(request, "lista_tabelas.html", {'context': context})


def delete_object(request, tabela, id):

    if (tabela=='disciplina'):
        obj = Disciplina.objects.get(id=id)
    elif (tabela=='disciplina_ofertada'):
        obj = DisciplinaOfertada.objects.get(id=id)
    elif (tabela=='unidade_federativa'):
        obj = UnidadeFederativa.objects.get(id=id)
    elif (tabela=='sexo'):
        obj = Sexo.objects.get(id=id)
    elif (tabela=='etnia'):
        obj = Etnia.objects.get(id=id)
    elif (tabela=='estado_civil'):
        obj = EstadoCivil.objects.get(id=id)
    elif (tabela=='vinculo'):
        obj = Vinculo.objects.get(id=id)
    elif (tabela=='status'):
        obj = StatusOptions.objects.get(id=id)
    elif (tabela=='linha_pesquisa'):
        obj = LinhaPesquisa.objects.get(id=id)
    elif (tabela=='instituicao'):
        obj = Instituicao.objects.get(id=id)
    elif (tabela=='colegio'):
        obj = Colegio.objects.get(id=id)
    elif (tabela=='instituicao_residencia'):
        obj = InstituicaoResidencia.objects.get(id=id)
    elif (tabela=='grau'):
        obj = Grau.objects.get(id=id)
    elif (tabela=='linguas'):
        obj = Linguas.objects.get(id=id)
    elif (tabela=='agencia_fomento'):
        obj = AgenciaFomento.objects.get(id=id)
    
    try:
        obj.delete()
        messages.success(request, 'Valor deletado com sucesso!')

    except:
        messages.warning(request, 'Este valor está sendo usado em algum objeto!')
    return redirect('config:lista_tabelas')


def edit_object(request, tabela, id):

    if (tabela=='disciplina'):
        obj = Disciplina.objects.get(id=id)
        form = DisciplinaForm(instance=obj)
        if(request.method == 'POST'):
            form = DisciplinaForm(request.POST, instance=obj)
            
    elif (tabela=='disciplina_ofertada'):
        obj = DisciplinaOfertada.objects.get(id=id)
        form = DisciplinaOfertadaForm(instance=obj)        
        if(request.method == 'POST'):
            form = DisciplinaOfertadaForm(request.POST, instance=obj)
            
    elif (tabela=='unidade_federativa'):
        obj = UnidadeFederativa.objects.get(id=id)
        form = UnidadeFederativaForm(instance=obj)
        if(request.method == 'POST'):
            form = UnidadeFederativaForm(request.POST, instance=obj)
    
    elif (tabela=='sexo'):
        obj = Sexo.objects.get(id=id)
        form = SexoForm(instance=obj)
        if(request.method == 'POST'):
            form = SexoForm(request.POST, instance=obj)
    
    elif (tabela=='etnia'):
        obj = Etnia.objects.get(id=id)
        form = EtniaForm(instance=obj)
        if(request.method == 'POST'):
            form = EtniaForm(request.POST, instance=obj)
    
    elif (tabela=='estado_civil'):
        obj = EstadoCivil.objects.get(id=id)
        form = EstadoCivilForm(instance=obj)
        if(request.method == 'POST'):
            form = EstadoCivilForm(request.POST, instance=obj)
    
    elif (tabela=='vinculo'):
        obj = Vinculo.objects.get(id=id)
        form = VinculoForm(instance=obj)
        if(request.method == 'POST'):
            form = VinculoForm(request.POST, instance=obj)
    
    elif (tabela=='status'):
        obj = StatusOptions.objects.get(id=id)
        form = StatusOptionsForm(instance=obj)
        if(request.method == 'POST'):
            form = StatusOptionsForm(request.POST, instance=obj)
    
    elif (tabela=='linha_pesquisa'):
        obj = LinhaPesquisa.objects.get(id=id)
        form = LinhaPesquisaForm(instance=obj)
        if(request.method == 'POST'):
            form = LinhaPesquisaForm(request.POST, instance=obj)
    
    elif (tabela=='instituicao'):
        obj = Instituicao.objects.get(id=id)
        form = InstituicaoForm(instance=obj)
        if(request.method == 'POST'):
            form = InstituicaoForm(request.POST, instance=obj)
    
    elif (tabela=='colegio'):
        obj = Colegio.objects.get(id=id)
        form = ColegioForm(instance=obj)
        if(request.method == 'POST'):
            form = ColegioForm(request.POST, instance=obj)
    
    elif (tabela=='instituicao_residencia'):
        obj = InstituicaoResidencia.objects.get(id=id)
        form = InstituicaoResidenciaForm(instance=obj)
        if(request.method == 'POST'):
            form = InstituicaoResidenciaForm(request.POST, instance=obj)
    
    elif (tabela=='grau'):
        obj = Grau.objects.get(id=id)
        form = GrauForm(instance=obj)
        if(request.method == 'POST'):
            form = GrauForm(request.POST, instance=obj)
    
    elif (tabela=='linguas'):
        obj = Linguas.objects.get(id=id)
        form = LinguasForm(instance=obj)
        if(request.method == 'POST'):
            form = LinguasForm(request.POST, instance=obj)
    
    elif (tabela=='agencia_fomento'):
        obj = AgenciaFomento.objects.get(id=id)
        form = AgenciaFomentoForm(instance=obj)
        if(request.method == 'POST'):
            form = AgenciaFomentoForm(request.POST, instance=obj)
    
    try:
        if(form.is_valid()):
                form.save()
                messages.success(request, 'Edição efetuada com sucesso com sucesso!')
                return redirect('config:lista_tabelas')

    except:
        messages.warning(request, 'Este valor está sendo usado em algum objeto!')

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Editar Tabela'})