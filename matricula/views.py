from django.shortcuts import render, redirect, HttpResponse
from colegiado.models import Colegiado
from colegiado.forms import ColegiadoForm
from .forms import AfastamentoForm, BolsaForm, InscricaoForm, \
                    MatriculaForm, ProbatorioForm, TrabalhoFinalForm, \
                    InscricaoProbatorioForm, VersaoFinalForm, NotaForm, \
                    LinhaPesquisaForm, OrientacaoForm, ExameLinguasForm, \
                    EditaInscricaoProbatorioForm, EditaInscricaoForm
from .models import Afastamento, Bolsa, Matricula, Probatorio, Inscricao, \
                    TrabalhoFinal, Orientacao
from config.models import StatusOptions, LinhaPesquisa
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from datetime            import datetime
from faker import Factory
from datetime import datetime
from dateutil.relativedelta import relativedelta  

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def render_pdf_view(request, matricula):

    matricula = Matricula.objects.get(id=matricula)

    template_path = 'historico_template.html'
    context = {'matricula': matricula, 'data': datetime.now().date().strftime("%d/%m/%Y")}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="historico_{matricula.numero}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def prorroga_data_limite_probatorio(request, probatorio):
    probatorio = Probatorio.objects.get(id=probatorio)
    print(f'Probatotio data limite: {probatorio.data_limite}')
    probatorio.data_limite = str(datetime(year=probatorio.data_limite.year+2, month=probatorio.data_limite.month, day=probatorio.data_limite.day).date())
    print(f'Probatotio data limite atualizada: {probatorio.data_limite}')
    
    probatorio.save()

    messages.success(request, 'Data limite atualizada com sucesso!')
    return redirect('matricula:detalhe_probatorio', probatorio.slug)

def cadastra_matricula(request, probatorio=None):
    print(probatorio)
    if probatorio:
        probatorio = Probatorio.objects.get(id=probatorio)
        form = MatriculaForm(initial={'probatorio':probatorio, 'grau':probatorio.grau, 'dt_matricula': datetime.today().date})
    else:
        form = MatriculaForm(initial={'dt_matricula': datetime.today().date})

    if(request.method == 'POST'):
        form = MatriculaForm(request.POST)
        if(form.is_valid()):
            
            status_opcao = StatusOptions.objects.get_or_create(status_options='Ativo', defaults={'cor': Factory.create().hex_color()})

            nova_matricula = Matricula.objects.create(
                numero = form.cleaned_data['numero'],
                probatorio = form.cleaned_data['probatorio'],
                requisita_bolsa = form.cleaned_data['requisita_bolsa'],
                cotista = form.cleaned_data['cotista'],
                grau = form.cleaned_data['grau'],
                dt_matricula = form.cleaned_data['dt_matricula'],
                cadastrado_por = User.objects.get(pk=request.user.id),
            )
            try:
                trab_final_prob = TrabalhoFinal.objects.get(probatorio=nova_matricula.probatorio)
            except:
                trab_final_prob = None            
            
            if trab_final_prob is not None:
                trab_final_prob.matricula = nova_matricula
                trab_final_prob.save()
            
            if nova_matricula.probatorio.linha_pesquisa is not None:
                nova_matricula.linha_pesquisa = nova_matricula.probatorio.linha_pesquisa

            Inscricao.objects.filter(probatorio=nova_matricula.probatorio).update(matricula=nova_matricula)

            edita_aluno = nova_matricula.probatorio.aluno
            status_aluno = edita_aluno.status
            status_aluno.status = status_opcao[0]
            status_aluno.save()
            edita_aluno.save()
            edita_probatorio = nova_matricula.probatorio
            edita_probatorio.probatorio = False
            edita_probatorio.save()
            nova_matricula.save()
            messages.success(request, 'Nova matrícula cadastrado com sucesso!')
            return redirect('matricula:detalhe_matricula', nova_matricula.slug)
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastrar Matricula'})

def lista_matricula(request):
    matriculas = Matricula.objects.all().order_by('probatorio')
    total = matriculas.count()

    busca = request.GET.get('search')
    if busca:
        matricula_lists = Matricula.objects.filter(Q(numero__icontains = busca)| Q(probatorio__aluno__nome__icontains = busca))
        paginator = Paginator(matricula_lists, 15)
        page = request.GET.get('page')
        matriculas = paginator.get_page(page)    

    return render(request, 'lista_matricula.html' , {'matriculas': matriculas, 'busca': busca, 'total':total, 'pagina':'Pesquisar Matrícula'})

def detalhe_matricula(request, matricula):
    
    matricula = Matricula.objects.get(id=matricula)
    bolsas = Bolsa.objects.filter(matricula=matricula)
    afastamentos = Afastamento.objects.filter(matricula=matricula)
    inscricoes = Inscricao.objects.filter(matricula=matricula)

    colegiados = Colegiado.objects.filter(matricula_membro=matricula)
    membro = colegiados.last
    form_colegiado = ColegiadoForm()

    if request.method == 'POST':
        form_colegiado = ColegiadoForm(request.POST)
        if form_colegiado.is_valid():
            novo_colegiado = Colegiado.objects.create(
                colegiado_data_entrada = form_colegiado.cleaned_data['colegiado_data_entrada'],
                colegiado_data_saida = form_colegiado.cleaned_data['colegiado_data_saida'],
                status_membro = form_colegiado.cleaned_data['status_membro'],
                matricula_membro = matricula
            )
            novo_colegiado.save()
            messages.success(request, 'Colegiado atualizado com sucesso!')
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)
    
    try:
        trabalho_final = TrabalhoFinal.objects.get(matricula=matricula)
    except TrabalhoFinal.DoesNotExist:
        trabalho_final = None

    return render(request, 'detalhe_matricula.html', {'matricula':matricula, 'bolsas': bolsas, 'afastamentos': afastamentos, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'colegiados': colegiados, 'membro': membro, 'form_colegiado': form_colegiado}) 

def cadastra_probatorio(request):
    form = ProbatorioForm()

    if(request.method == 'POST'):
        form = ProbatorioForm(request.POST)
        if(form.is_valid()):
            
            status_opcao = StatusOptions.objects.get_or_create(status_options='Probatório', defaults={'cor': Factory.create().hex_color()})

            novo_probatorio = Probatorio.objects.create(
                data_inscricao = form.cleaned_data['data_inscricao'],
                aluno = form.cleaned_data['aluno'],
                nota_selecao = form.cleaned_data['nota_selecao'],
                cadastrado_por = User.objects.get(pk=request.user.id),
            )
            aluno_probatorio = novo_probatorio.aluno
            status_aluno = aluno_probatorio.status
            status_aluno.status = status_opcao[0]
            status_aluno.save()
            aluno_probatorio.save()
            novo_probatorio.save()

            messages.success(request, 'Novo probatório cadastrado com sucesso!')
            return redirect('matricula:detalhe_probatorio', novo_probatorio.slug)
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastrar Probatório'})

def lista_probatorio(request):
    probatorios = Probatorio.objects.all().order_by('aluno')
    total = probatorios.count()

    busca = request.GET.get('search')
    if busca:
        probatorio_lists = Probatorio.objects.filter(Q(aluno__cpf__icontains = busca)| Q(aluno__nome__icontains = busca))
        paginator = Paginator(probatorio_lists, 15)
        page = request.GET.get('page')
        probatorios = paginator.get_page(page)    

    return render(request, 'lista_matricula.html' , {'matriculas': probatorios, 'busca': busca, 'total':total, 'pagina':'Pesquisar Probatório'})

def detalhe_probatorio(request, probatorio):
    
    probatorio = Probatorio.objects.get(id=probatorio)
    inscricoes = Inscricao.objects.filter(probatorio=probatorio.slug)
    form_exame = ExameLinguasForm()
    form_nota = NotaForm()
    form_edita_nota = NotaForm(instance=probatorio.nota)
    

    data_limite = datetime(year=probatorio.data_limite.year, 
                           month=probatorio.data_limite.month, 
                           day=probatorio.data_limite.day)

    print(f'Data limite: {probatorio.data_limite}')
    data_final_remanescente = data_limite - datetime.now() 
    print(data_final_remanescente)

    try:
        trabalho_final = TrabalhoFinal.objects.get(probatorio=probatorio)
    except TrabalhoFinal.DoesNotExist:
        trabalho_final = None


    if request.method == 'POST' and "btn_edita_nota_probatorio" in request.POST:
        form_edita_nota = NotaForm(request.POST, instance=probatorio.nota)
        if (form_edita_nota.is_valid()):
            form_edita_nota.save()
            messages.success(request, 'Nota do probatório cadastrado com sucesso!')
            return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota, 'form_edita_nota': form_edita_nota, 'data_final_remanescente': data_final_remanescente.days}) 

    if(request.method == 'POST' and "btn_nota_probatorio" in request.POST):
        form_nota = NotaForm(request.POST)
        if(form_nota.is_valid()):
            nova_nota = form_nota.save(commit=False)
            nova_nota.probatorio = probatorio
            probatorio.nota = nova_nota
            nova_nota.save()
            probatorio.save()
            messages.success(request, 'Nota do probatório cadastrado com sucesso!')
            return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota, 'form_edita_nota': form_edita_nota, 'data_final_remanescente': data_final_remanescente.days}) 

    if(request.method == 'POST' and "btn_nota_exame" in request.POST):
        form_exame = ExameLinguasForm(request.POST)
        if(form_exame.is_valid()):
            nova_nota = form_exame.save()
            nova_nota.probatorio.add(probatorio)
            # nova_nota.save()
            messages.success(request, 'Exame de linguas cadastrado com sucesso!')
            return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota, 'form_edita_nota': form_edita_nota, 'data_final_remanescente': data_final_remanescente.days}) 


    return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota, 'form_edita_nota': form_edita_nota, 'data_final_remanescente': data_final_remanescente.days}) 

def cadastra_bolsa(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    
    form = BolsaForm()

    if(request.method == 'POST'):
        form = BolsaForm(request.POST)
        if(form.is_valid()):
            nova_bolsa = Bolsa.objects.create(
                nome = form.cleaned_data['nome'],
                bolsa_agencia = form.cleaned_data['bolsa_agencia'],
                dt_inicio = form.cleaned_data['dt_inicio'],
                dt_final = form.cleaned_data['dt_final'],                                
                matricula = matricula
            )

            nova_bolsa.save()
            messages.success(request, 'Nova bolsa cadastrada com sucesso!')
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastrar Bolsa', 'matricula': matricula})

def cadastra_afastamento(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    form = AfastamentoForm()

    if(request.method == 'POST'):
        form = AfastamentoForm(request.POST)
        if(form.is_valid()):
            novo_afastamento = Afastamento.objects.create(
                motivo = form.cleaned_data['motivo'],
                saida = form.cleaned_data['saida'],
                retorno = form.cleaned_data['retorno'],
                matricula = matricula
            )

            novo_afastamento.save()
            messages.success(request, 'Novo afastamento cadastrado com sucesso!')
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastrar Afastamento', 'matricula': matricula})

def cadastra_inscricao(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    form = InscricaoForm()

    if(request.method == 'POST'):
        form = InscricaoForm(request.POST)
        if(form.is_valid()):
            nova_inscricao = Inscricao.objects.create(
                disciplina_ofertada = form.cleaned_data['disciplina_ofertada'],
                nota = form.cleaned_data['nota'],
                situacao = form.cleaned_data['situacao'],
                matricula = matricula,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )
            messages.success(request, 'Inscrição efetuado com sucesso!')
            nova_inscricao.save()
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastrar Inscrição', 'matricula': matricula})

def cadastra_inscricao_probatorio(request, probatorio):
    probatorio = Probatorio.objects.get(slug=probatorio)
    form = InscricaoProbatorioForm()

    if(request.method == 'POST'):
        form = InscricaoProbatorioForm(request.POST)
        if(form.is_valid()):
            nova_inscricao = Inscricao.objects.create(
                disciplina_ofertada = form.cleaned_data['disciplina_ofertada'],
                nota = form.cleaned_data['nota'],
                situacao = form.cleaned_data['situacao'],
                probatorio = probatorio,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            nova_inscricao.save()
            return redirect('matricula:detalhe_probatorio', probatorio=probatorio.slug) 

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Inscrição em Probatório', 'probatorio':probatorio})

def cadastra_trabalho_final(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    trabalho_final_form = TrabalhoFinalForm()
    linha_pesquisa_form = LinhaPesquisaForm()

    if(request.method == 'POST'):
        trabalho_final_form = TrabalhoFinalForm(request.POST)
        linha_pesquisa_form = LinhaPesquisaForm(request.POST)
        if(trabalho_final_form.is_valid() and linha_pesquisa_form.is_valid()):
            novo_trabalho_final = TrabalhoFinal.objects.create(
                titulo = trabalho_final_form.cleaned_data['titulo'],
                resumo = trabalho_final_form.cleaned_data['resumo'],
                matricula = matricula,
                probatorio = matricula.probatorio,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            matricula.linha_pesquisa = linha_pesquisa_form.cleaned_data['linha_pesquisa']
            matricula.save()
            novo_trabalho_final.save()

            return redirect('matricula:detalhe_trabalho_final', matricula.slug)
    
    return render(request, 'cadastra_trabalho_final.html', {'trabalho_final_form':trabalho_final_form, 'linha_pesquisa_form':linha_pesquisa_form, 'pagina':'Cadastra Trabalho Final'})

def cadastra_orientacao(request, matricula, trabalho_final):
    matricula = Matricula.objects.get(slug=matricula)
    form = OrientacaoForm()

    if(request.method == 'POST'):
        form = OrientacaoForm(request.POST)
        
        if(form.is_valid()):
            nova_orientacao = form.save(commit=False)
            nova_orientacao.trabalho_final = matricula.matricula_trabalho_final
            nova_orientacao.save()
            return redirect("matricula:detalhe_trabalho_final", matricula.slug)

    return render(request, 'cadastra_orientacao.html', {'form': form, 'matricula': matricula, 'trabalho_final': matricula.matricula_trabalho_final, 'pagina': 'Cadastrar Orientadores'})

def cadastra_orientacao_probatorio(request, probatorio, trabalho_final):
    probatorio = Probatorio.objects.get(slug=probatorio)
    form = OrientacaoForm()

    if(request.method == 'POST'):
        form = OrientacaoForm(request.POST)
        
        if(form.is_valid()):
            nova_orientacao = form.save(commit=False)
            nova_orientacao.trabalho_final = probatorio.probatorio_trabalho_final
            nova_orientacao.save()
            return redirect("matricula:detalhe_trabalho_final_probatorio", probatorio.slug)

    return render(request, 'cadastra_orientacao_probatorio.html', {'form': form, 'probatorio': probatorio, 'trabalho_final': probatorio.probatorio_trabalho_final, 'pagina': 'Cadastrar Orientadores'})

def detalhe_trabalho_final(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    trabalho_final = TrabalhoFinal.objects.get(matricula=matricula)
    coorientador = None # Implementar coorientador

    versao_final_form = VersaoFinalForm()
    nota_form = NotaForm()

    if trabalho_final.versao_final is None:
        
        if request.method == 'POST' and 'versao_sub' in request.POST:
            versao_final_form = VersaoFinalForm(request.POST)
            if versao_final_form.is_valid():

                status_opcao = StatusOptions.objects.get_or_create(status_options='Titulado', defaults={'cor': Factory.create().hex_color()})

                nova_versao = versao_final_form.save(commit=False)
                trabalho_final.versao_final = nova_versao
                nova_versao.save()
                trabalho_final.save()
                aluno_status = matricula.probatorio.aluno.status
                aluno_status.status = status_opcao[0]
                aluno_status.save()
                messages.success(request, 'Versão final cadastrada e status do aluno alterado para Titulado')
                return redirect("matricula:detalhe_trabalho_final", matricula=matricula.slug)
    else:
        versao_final_form = None

    if trabalho_final.nota is None:
        
        if request.method == 'POST' and 'nota_sub' in request.POST:
            nota_form = NotaForm(request.POST)
            if nota_form.is_valid():
                nova_nota = nota_form.save(commit=False)
                trabalho_final.nota = nova_nota
                nova_nota.save()
                trabalho_final.save()
                messages.success(request, 'Nota final cadastrada!')
                return redirect("matricula:detalhe_trabalho_final", matricula=matricula.slug)
    else:
        nota_form = None

    return render(request, 'detalhe_trabalho_final.html', {'matricula':matricula, 'pagina':'Trabalho Final', 'trabalho_final':trabalho_final, 'coorientador': coorientador, 'form_versao': versao_final_form, 'form_nota':nota_form})

def cadastra_trabalho_probatorio(request, probatorio):

    probatorio = Probatorio.objects.get(slug=probatorio)
    trabalho_final_form = TrabalhoFinalForm()
    linha_pesquisa_form = LinhaPesquisaForm()


    if(request.method == 'POST'):
        trabalho_final_form = TrabalhoFinalForm(request.POST)
        linha_pesquisa_form = LinhaPesquisaForm(request.POST)

        if(trabalho_final_form.is_valid() and linha_pesquisa_form.is_valid()):
            novo_trabalho_final = TrabalhoFinal.objects.create(
                titulo = trabalho_final_form.cleaned_data['titulo'],
                resumo = trabalho_final_form.cleaned_data['resumo'],
                probatorio = probatorio,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )
            probatorio.linha_pesquisa = linha_pesquisa_form.cleaned_data['linha_pesquisa']
            probatorio.save()
            novo_trabalho_final.save()

            return redirect('matricula:detalhe_trabalho_final_probatorio', probatorio.slug)
    
    return render(request, 'cadastra_trabalho_final.html', {'trabalho_final_form':trabalho_final_form, 'linha_pesquisa_form': linha_pesquisa_form,  'pagina':'Cadastra Trabalho Final'})

def detalhe_trabalho_final_probatorio(request, probatorio):
    probatorio = Probatorio.objects.get(slug=probatorio)
    trabalho_final = TrabalhoFinal.objects.get(probatorio=probatorio)
    coorientador = None # Implementar coorientador


    return render(request, 'detalhe_trabalho_final_probatorio.html', {'probatorio':probatorio, 'pagina':'Trabalho Final', 'trabalho_final':trabalho_final, 'coorientador': coorientador})

def edita_inscricao_probatorio(request, probatorio, inscricao):
    probatorio = Probatorio.objects.get(id=probatorio)
    inscricao = Inscricao.objects.get(id=inscricao)
    form = EditaInscricaoProbatorioForm(instance=inscricao)

    if request.method == "POST":
        form = EditaInscricaoProbatorioForm(request.POST, instance=inscricao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscrição atualizada com sucesso!')            
            return redirect('matricula:detalhe_probatorio', probatorio=probatorio.slug)
    
    return render(request, "cadastra_matricula.html", {"form": form, "probatorio": probatorio, "pagina": "Edita Inscrição em Probatório"})

def edita_inscricao(request, matricula, inscricao):
    matricula = Matricula.objects.get(id=matricula)
    inscricao = Inscricao.objects.get(id=inscricao)
    form = EditaInscricaoForm(instance=inscricao)

    if request.method == "POST":
        form = EditaInscricaoForm(request.POST, instance=inscricao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscrição atualizada com sucesso!')            
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)
    
    return render(request, "cadastra_matricula.html", {"form": form, "matricula": matricula, "pagina": "Edita Inscrição em Matrícula"})

def deleta_orientador(request, trabalho_final, orientacao):
    orientacao = Orientacao.objects.get(id=orientacao)
    probatorio = orientacao.trabalho_final.probatorio.slug
    orientacao.delete()
    messages.success(request, 'Orientador removido com sucesso!')            
    return redirect('matricula:detalhe_trabalho_final_probatorio', probatorio=probatorio)


def edita_desistencia(request, probatorio):

    status_opcao = StatusOptions.objects.get_or_create(status_options='Desistência', defaults={'cor': Factory.create().hex_color()})

    probatorio = Probatorio.objects.get(id=probatorio)
    aluno_status = probatorio.aluno.status
    aluno_status.status = status_opcao[0]
    aluno_status.save()

    messages.success(request, 'Alterado o status para desistência.')
    return redirect("matricula:detalhe_probatorio", probatorio=probatorio.slug)


def edita_colegiado(request, colegiado):
    colegiado = Colegiado.objects.get(id=colegiado)
    matricula = colegiado.matricula_membro
    form_colegiado = ColegiadoForm(instance=colegiado)

    if request.method == 'POST':
        form_colegiado = ColegiadoForm(request.POST, instance=colegiado)
        if form_colegiado.is_valid():
            form_colegiado.save()
            messages.success(request, 'Colegiado atualizado com sucesso!')
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)
    return render(request, 'edita_colegiado_matricula.html', {'form': form_colegiado, 'matricula':matricula})

