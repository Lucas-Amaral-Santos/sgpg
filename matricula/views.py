from django.shortcuts import render, redirect
from .forms import AfastamentoForm, BolsaForm, InscricaoForm, MatriculaForm, ProbatorioForm, TrabalhoFinalForm
from .models import Afastamento, Bolsa, Matricula, Probatorio, Inscricao, TrabalhoFinal
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def cadastra_matricula(request):
    form = MatriculaForm()

    if(request.method == 'POST'):
        form = MatriculaForm(request.POST)
        if(form.is_valid()):
            nova_matricula = Matricula.objects.create(
                numero = form.cleaned_data['numero'],
                probatorio = form.cleaned_data['probatorio'],
                requisita_bolsa = form.cleaned_data['requisita_bolsa'],
                cadastrado_por = User.objects.get(pk=request.user.id),
            )
            edita_probatorio = nova_matricula.probatorio
            edita_probatorio.probatorio = False
            edita_probatorio.save()
            nova_matricula.save()
            return redirect('/')
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Matricula'})


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
            novo_probatorio = Probatorio.objects.create(
                data_inscricao = form.cleaned_data['data_inscricao'],
                nota = form.cleaned_data['nota'],
                aluno = form.cleaned_data['aluno'],
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            novo_probatorio.save()

            return redirect('/')
    
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

            return redirect('/')
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Bolsa'})

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

            return redirect('/')
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Afastamento'})

def cadastra_inscricao(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    form = InscricaoForm()

    if(request.method == 'POST'):
        form = InscricaoForm(request.POST)
        if(form.is_valid()):
            nova_inscricao = Inscricao.objects.create(
                disciplina_ofertada = form.cleaned_data['disciplina_ofertada'],
                nota = form.cleaned_data['nota'],
                matricula = matricula,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            nova_inscricao.save()
            return redirect('/')

    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Inscrição'})

def cadastra_trabalho_final(request, matricula):
    matricula = Matricula.objects.get(slug=matricula)
    form = TrabalhoFinalForm()

    if(request.method == 'POST'):
        form = TrabalhoFinalForm(request.POST)
        if(form.is_valid()):
            novo_trabalho_final = TrabalhoFinal.objects.create(
                titulo = form.cleaned_data['titulo'],
                data = form.cleaned_data['data'],
                resumo = form.cleaned_data['resumo'],
                resultado = form.cleaned_data['resultado'],
                diploma = form.cleaned_data['diploma'],
                dt_diploma = form.cleaned_data['dt_diploma'],
                versao_final = form.cleaned_data['versao_final'],
                dt_versao = form.cleaned_data['dt_versao'],
                matricula = matricula,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            novo_trabalho_final.save()

            return redirect('/')
    
    return render(request, 'cadastra_matricula.html', {'form':form, 'pagina':'Cadastra Trabalho Final'})