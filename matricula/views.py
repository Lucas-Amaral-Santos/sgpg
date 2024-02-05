from django.shortcuts import render, redirect, HttpResponse
from .forms import AfastamentoForm, BolsaForm, InscricaoForm, \
                    MatriculaForm, ProbatorioForm, TrabalhoFinalForm, \
                    InscricaoProbatorioForm, VersaoFinalForm, NotaForm, \
                    LinhaPesquisaForm, OrientacaoForm, ExameLinguasForm, \
                    EditaInscricaoProbatorioForm, EditaInscricaoForm
from .models import Afastamento, Bolsa, Matricula, Probatorio, Inscricao, \
                    TrabalhoFinal, InscricaoProbatorio, Orientacao
from config.models import StatusOptions, LinhaPesquisa
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from datetime            import datetime
from faker import Factory

def gera_historico(request, matricula):

    matricula = Matricula.objects.get(id=matricula)
    bolsas = Bolsa.objects.filter(matricula=matricula)
    afastamentos = Afastamento.objects.filter(matricula=matricula)
    inscricoes = Inscricao.objects.filter(matricula=matricula)
    try:
        trabalho_final = TrabalhoFinal.objects.get(matricula=matricula)
    except TrabalhoFinal.DoesNotExist:
        trabalho_final = None


    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    p.setFont("Helvetica", 9)
    # Tela (595.27,841.89)
    
    width = 595.27
    height = 841.89
    margin = 30


    # Desenhando o cabeçalho top-left
    p.line(margin, height-margin, width-margin-200, height-margin)
    p.line(margin, height-margin, margin, height-margin-70)
    
    p.drawString(75, height-margin-20, "UNIVERSIDADE FEDERAL FLUMINENSE")
    p.drawString(150, height-margin-35, "CENTRO")
    p.drawString(75, height-margin-50, "PROGRAMA DE PÓS-GRADUAÇÃO EM")
    p.line(margin,height-margin-70, width-margin-200, height-margin-70)
    p.line(width-margin-200, height-margin, width-margin-200, height-margin-70)

    p.line(margin,height-105, width-margin-200, height-105)
    p.line(margin,height-105, margin, height-125)
    p.drawString(70, height-120, "HISTÓRICO ESCOLAR / PÓS-GRADUAÇÃO")
    p.line(margin,height-125, width-margin-200, height-125)
    p.line(width-margin-200,height-105, width-margin-200, height-125)


    p.line(width-margin-190, height-margin, width-margin, height-margin)
    p.line(width-margin-190, height-margin, width-margin-190, height-125)


    p.line(width-margin-190, height-125, width-margin, height-125)
    p.line(width-margin, height-margin, width-margin, height-125)



    # Informações do aluno
    p.line(margin, 0.845*height, width-margin, 0.845*height)
    p.line(margin, 0.845*height, margin, 0.75*height)

    p.drawString(1.2*margin, 0.83*height, "ALUNO   " + matricula.probatorio.aluno.nome)
    p.drawString(1.2*margin, 0.81*height, "MATRÍCULA   " + matricula.numero)
    p.drawString(6*margin, 0.81*height, "NACIONALIDADE   " + matricula.probatorio.aluno.nacionalidade)
    p.drawString(12*margin, 0.81*height, "DATA NASCIMENTO   " + matricula.probatorio.aluno.dt_nascimento.strftime("%d/%m/%Y"))
    p.drawString(1.2*margin, 0.79*height, "CÉDULA DE IDENTIFICAÇÃO   " + matricula.probatorio.aluno.identidade)
    p.drawString(8*margin, 0.79*height, "ORGÃO EXPEDITOR   " + matricula.probatorio.aluno.identidade_orgao)
    p.drawString(13*margin, 0.79*height, "ESTADO EXPEDITOR   " + matricula.probatorio.aluno.identidade_uf)
    p.drawString(1.2*margin, 0.77*height, "CIC   " + matricula.probatorio.aluno.identidade_uf)

    p.line(margin, 0.75*height, width-margin, 0.75*height)
    p.line(width-margin, 0.845*height, width-margin, 0.75*height)

    # Informações da Matrícula
    p.line(margin, 0.745*height, width-margin, 0.745*height)
    p.line(width-margin, 0.745*height, width-margin, 0.625*height)
    p.drawString(1.2*margin, 0.73*height, "CURSO   " + matricula.probatorio.aluno.nome)
    p.drawString(1.2*margin, 0.71*height, "ÁREA DE CONCENTRAÇÃO/")
    p.drawString(1.2*margin, 0.70*height, "CAMPO DE CONCENTRAÇÃO")
    p.drawString(6*margin, 0.705*height, "[valor]")
    p.drawString(1.2*margin, 0.68*height, "CONCEITO CAPES")
    p.drawString(6*margin, 0.68*height, "[valor]")
    
    p.line(margin, 0.675*height, width-margin, 0.675*height)
    p.drawString(1.2*margin, 0.660*height, "RESULTADO DO EXAME DE SELEÇÃO")
    p.drawString(7*margin, 0.660*height, "[valor]")
    p.line(margin, 0.656*height, width-margin, 0.656*height)


    p.drawString(1.2*margin, 0.645*height, "EXAME(S) DE LÍNGUA")
    p.drawString(7*margin, 0.645*height, "[valor]")
    p.line(margin, 0.640*height, width-margin, 0.640*height)

    p.drawString(1.2*margin, 0.629*height, "MESIANO DE INGRESSO NO CURSO")
    p.drawString(7*margin, 0.629*height, "[valor]")
    p.line(margin, 0.625*height, width-margin, 0.625*height)

    p.line(margin, 0.745*height, margin, 0.625*height)

    p.line(margin, 0.615*height, width-margin, 0.615*height)
    p.line(margin, 0.615*height, margin, margin)
    p.line(width-margin, 0.615*height, width-margin, margin)

    p.line(margin,margin, width-margin, margin)

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='historico'+str(matricula.numero)+'.pdf')

def cadastra_matricula(request):
    form = MatriculaForm()

    if(request.method == 'POST'):
        form = MatriculaForm(request.POST)
        if(form.is_valid()):
            
            status_opcao = StatusOptions.objects.get_or_create(status_options='Ativo', defaults={'cor': Factory.create().hex_color()})

            nova_matricula = Matricula.objects.create(
                numero = form.cleaned_data['numero'],
                probatorio = form.cleaned_data['probatorio'],
                requisita_bolsa = form.cleaned_data['requisita_bolsa'],
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
    
    try:
        trabalho_final = TrabalhoFinal.objects.get(matricula=matricula)
    except TrabalhoFinal.DoesNotExist:
        trabalho_final = None

    

    return render(request, 'detalhe_matricula.html', {'matricula':matricula, 'bolsas': bolsas, 'afastamentos': afastamentos, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final}) 

def cadastra_probatorio(request):
    form = ProbatorioForm()

    if(request.method == 'POST'):
        form = ProbatorioForm(request.POST)
        if(form.is_valid()):
            
            status_opcao = StatusOptions.objects.get_or_create(status_options='Probatório', defaults={'cor': Factory.create().hex_color()})

            novo_probatorio = Probatorio.objects.create(
                data_inscricao = form.cleaned_data['data_inscricao'],
                aluno = form.cleaned_data['aluno'],
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
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Probatório'})

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
    inscricoes = InscricaoProbatorio.objects.filter(probatorio=probatorio.slug)
    form_exame = ExameLinguasForm()
    form_nota = NotaForm()
    try:
        trabalho_final = TrabalhoFinal.objects.get(probatorio=probatorio)
    except TrabalhoFinal.DoesNotExist:
        trabalho_final = None
    
    if(request.method == 'POST' and "btn_nota_probatorio" in request.POST):
        form_nota = NotaForm(request.POST)
        if(form_nota.is_valid()):
            nova_nota = form_nota.save(commit=False)
            nova_nota.probatorio = probatorio
            probatorio.nota = nova_nota
            nova_nota.save()
            probatorio.save()
            messages.success(request, 'Nota do probatório cadastrado com sucesso!')
            return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota}) 

    if(request.method == 'POST' and "btn_nota_exame" in request.POST):
        form_exame = ExameLinguasForm(request.POST)
        if(form_exame.is_valid()):
            nova_nota = form_exame.save()
            nova_nota.probatorio.add(probatorio)
            # nova_nota.save()
            messages.success(request, 'Exame de linguas cadastrado com sucesso!')
            return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota}) 


    return render(request, 'detalhe_probatorio.html', {'probatorio':probatorio, 'inscricoes':inscricoes, 'trabalho_final':trabalho_final, 'form_exame': form_exame, 'form_nota': form_nota}) 

def cadastra_bolsa(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    
    form = BolsaForm()

    if(request.method == 'POST'):
        form = BolsaForm(request.POST)
        if(form.is_valid()):
            nova_bolsa = Bolsa.objects.create(
                nome = form.cleaned_data['nome'],
                agencia = form.cleaned_data['agencia'],
                dt_inicio = form.cleaned_data['dt_inicio'],
                iniciacao_cientifica = form.cleaned_data['iniciacao_cientifica'],
                matricula = matricula
            )

            nova_bolsa.save()
            messages.success(request, 'Nova bolsa cadastrada com sucesso!')
            return redirect('matricula:detalhe_matricula', matricula=matricula.slug)
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Bolsa', 'matricula': matricula})

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
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Afastamento', 'matricula': matricula})

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

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Inscrição', 'matricula': matricula})

def cadastra_inscricao_probatorio(request, probatorio):
    probatorio = Probatorio.objects.get(slug=probatorio)
    form = InscricaoProbatorioForm()

    if(request.method == 'POST'):
        form = InscricaoProbatorioForm(request.POST)
        if(form.is_valid()):
            nova_inscricao = InscricaoProbatorio.objects.create(
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

            return redirect('matricula:detalhe_trabalho_final', probatorio.slug)
    
    return render(request, 'cadastra_trabalho_final.html', {'trabalho_final_form':trabalho_final_form, 'linha_pesquisa_form': linha_pesquisa_form,  'pagina':'Cadastra Trabalho Final'})

def detalhe_trabalho_final_probatorio(request, probatorio):
    probatorio = Probatorio.objects.get(slug=probatorio)
    trabalho_final = TrabalhoFinal.objects.get(probatorio=probatorio)
    coorientador = None # Implementar coorientador


    return render(request, 'detalhe_trabalho_final_probatorio.html', {'probatorio':probatorio, 'pagina':'Trabalho Final', 'trabalho_final':trabalho_final, 'coorientador': coorientador})

def edita_inscricao_probatorio(request, probatorio, inscricao):
    probatorio = Probatorio.objects.get(id=probatorio)
    inscricao = InscricaoProbatorio.objects.get(id=inscricao)
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
