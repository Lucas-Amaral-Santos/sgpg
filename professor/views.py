from django.shortcuts import render
from .forms import ProfessorForm, TrabalhoForm, PosDoutoradoForm, ColegiadoForm
from  .models import Professor, Trabalho, PosDoutorado, Colegiado
from django.contrib.auth.models import User

from aluno.models import Endereco, Titulacao
from aluno.forms import EnderecoForm, TitulacaoProfessorForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def cadastra_professor(request):
    form_professor = ProfessorForm()
    form_colegiado = ColegiadoForm()
    form_trabalho = TrabalhoForm()
    form_pos_doutorado = PosDoutoradoForm()
    form_endereco = EnderecoForm()
    form_titulacao = TitulacaoProfessorForm()

    print(request.user)

    if request.method == "POST":
        form_professor = ProfessorForm(request.POST)
        form_colegiado = ColegiadoForm(request.POST)
        form_trabalho = TrabalhoForm(request.POST)
        form_pos_doutorado = PosDoutoradoForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        form_titulacao = TitulacaoProfessorForm(request.POST)

        if form_professor.is_valid()and form_colegiado.is_valid() and form_trabalho.is_valid() and form_pos_doutorado.is_valid() and form_titulacao.is_valid() and form_endereco.is_valid():
            
            novo_colegiado = Colegiado.objects.create(
                colegiado_membro = form_colegiado.cleaned_data['colegiado_membro'],
                colegiado_data_entrada = form_colegiado.cleaned_data['colegiado_data_entrada'],
                colegiado_data_saida = form_colegiado.cleaned_data['colegiado_data_saida'],
            )

            novo_titulacao = Titulacao.objects.create(
                titulacao = form_titulacao.cleaned_data['titulacao'],
                titulacao_area = form_titulacao.cleaned_data['titulacao_area'],
                titulacao_ano = form_titulacao.cleaned_data['titulacao_ano'],
                uf = form_titulacao.cleaned_data['uf'],
                instituicao_titulacao = form_titulacao.cleaned_data['instituicao_titulacao'],
                obs_geral = form_titulacao.cleaned_data['obs_geral'],
            )
            
            novo_endereco = Endereco.objects.create(
                cep = form_endereco.cleaned_data['cep'],
                endereco = form_endereco.cleaned_data['endereco'],
                municipio = form_endereco.cleaned_data['municipio'],
                uf = form_endereco.cleaned_data['uf'],
                telefone1 = form_endereco.cleaned_data['telefone1'],
                telefone2 = form_endereco.cleaned_data['telefone2'],
            )

            novo_pos_doutorado = PosDoutorado.objects.create(
                concluido =  form_pos_doutorado.cleaned_data['concluido'],
                ano_inicio = form_pos_doutorado.cleaned_data['ano_inicio'],
                ano_fim = form_pos_doutorado.cleaned_data['ano_fim'],
                instituicao_posdoc = form_pos_doutorado.cleaned_data['instituicao_posdoc'],
                pais = form_pos_doutorado.cleaned_data['pais'],
            )
            novo_trabalho = Trabalho.objects.create(
                instituicao_trabalho = form_trabalho.cleaned_data['instituicao_trabalho'],
                setor = form_trabalho.cleaned_data['setor'],
                admissao = form_trabalho.cleaned_data['admissao'],
                cargo = form_trabalho.cleaned_data['cargo'],
                telefone = form_trabalho.cleaned_data['telefone'],
                categoria = form_trabalho.cleaned_data['categoria'],
                email = form_trabalho.cleaned_data['email'],
            )
            novo_professor = Professor.objects.create(
                nome = form_professor.cleaned_data['nome'],
                sexo = form_professor.cleaned_data['sexo'],
                dt_nascimento = form_professor.cleaned_data['dt_nascimento'],
                nacionalidade = form_professor.cleaned_data['nacionalidade'],
                naturalidade = form_professor.cleaned_data['naturalidade'],
                cpf = form_professor.cleaned_data['cpf'],
                identidade = form_professor.cleaned_data['identidade'], 
                identidade_orgao = form_professor.cleaned_data['identidade_orgao'],    
                tipo_docente = form_professor.cleaned_data['tipo_docente'],   
                trabalho = novo_trabalho,
                pos_doutorado = novo_pos_doutorado,
                titulacao = novo_titulacao,
                endereco = novo_endereco,
                membro_colegiado = novo_colegiado,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )
            novo_colegiado.save()
            novo_titulacao.save()
            novo_endereco.save()
            novo_pos_doutorado.save()
            novo_trabalho.save()
            novo_professor.save()
            novo_professor.save()

    return render(request, "cadastra_professor.html", {'form_professor': form_professor, 'form_colegiado': form_colegiado, 'form_trabalho': form_trabalho, 'form_pos_doutorado':form_pos_doutorado, 'form_endereco': form_endereco, 'form_titulacao': form_titulacao})

def lista_professor(request):
    professores = Professor.objects.all().order_by('nome')
    total = professores.count()

    busca = request.GET.get('search')
    if busca:
        professor_lists = Professor.objects.filter(Q(nome__icontains = busca)| Q(cpf__icontains = busca))
        paginator = Paginator(professor_lists, 15)
        page = request.GET.get('page')
        professores = paginator.get_page(page)  

    return render(request, 'lista_professor.html' , {'professores': professores, 'busca': busca, 'total':total})