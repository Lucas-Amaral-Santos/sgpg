from django.shortcuts import render

from matricula.models import Matricula
from .forms import AlunoForm, EnderecoForm, GraduacaoForm, TrabalhoForm, ResidenciaForm, TitulacaoForm, EnsinoMedioForm
from .models import Aluno, Endereco, Graduacao, Trabalho, Residencia, Titulacao, EnsinoMedio
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def cadastra_aluno(request):
    form_aluno = AlunoForm()
    form_endereco = EnderecoForm()
    form_graduacao = GraduacaoForm()
    form_ensino_medio = EnsinoMedioForm()
    form_trabalho = TrabalhoForm()
    form_endereco_trabalho = EnderecoForm()
    form_residencia = ResidenciaForm()
    form_titulacao = TitulacaoForm()

    if request.method == "POST":
        form_aluno = AlunoForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        form_graduacao = GraduacaoForm(request.POST)
        form_ensino_medio = EnsinoMedioForm(request.POST)
        form_trabalho = TrabalhoForm(request.POST)
        form_endereco_trabalho = EnderecoForm(request.POST)
        form_residencia = ResidenciaForm(request.POST)
        form_titulacao = TitulacaoForm(request.POST)

        if form_aluno.is_valid() and \
            form_endereco.is_valid() and \
            form_graduacao.is_valid() and \
            form_trabalho.is_valid() and \
            form_endereco_trabalho.is_valid() and \
            form_residencia.is_valid() and \
            form_titulacao.is_valid() and \
            form_ensino_medio.is_valid():

            novo_ensino_medio = EnsinoMedio.objects.create(
                ensino_medio_instituicao = form_ensino_medio.cleaned_data['ensino_medio_instituicao'],
                ensino_medio_ano_inicio = form_ensino_medio.cleaned_data['ensino_medio_ano_inicio'],
                ensino_medio_ano_conclusao = form_ensino_medio.cleaned_data['ensino_medio_ano_conclusao'],
                ensino_medio_municipio = form_ensino_medio.cleaned_data['ensino_medio_municipio'],
                ensino_medio_tipo = form_ensino_medio.cleaned_data['ensino_medio_tipo'],
            )

            novo_titulacao = Titulacao.objects.create(
                titulacao = form_titulacao.cleaned_data['titulacao'],
                titulacao_area = form_titulacao.cleaned_data['titulacao_area'],
                titulacao_ano = form_titulacao.cleaned_data['titulacao_ano'],
                uf = form_titulacao.cleaned_data['uf'],
                data_qualificacao = form_titulacao.cleaned_data['data_qualificacao'],
                instituicao_titulacao = form_titulacao.cleaned_data['instituicao_titulacao'],
                obs_geral = form_titulacao.cleaned_data['obs_geral'],
            )

            novo_residencia = Residencia.objects.create(
                instituicao_residencia = form_residencia.cleaned_data['instituicao_residencia'],
                residencia_ano_inicio = form_residencia.cleaned_data['residencia_ano_inicio'],
                residencia_ano_fim = form_residencia.cleaned_data['residencia_ano_fim'],
                especialidade = form_residencia.cleaned_data['especialidade'],
                uf = form_residencia.cleaned_data['uf'],
            )
            
            novo_graduacao = Graduacao.objects.create(
                graduacao_area = form_graduacao.cleaned_data['graduacao_area'],
                instituicao = form_graduacao.cleaned_data['instituicao'],
                local = form_graduacao.cleaned_data['local'],
                graduacao_ano_inicio = form_graduacao.cleaned_data['graduacao_ano_inicio'],
                graduacao_ano_fim = form_graduacao.cleaned_data['graduacao_ano_fim'],
                bolsa_graduacao = form_graduacao.cleaned_data['bolsa_graduacao'],
                agencia = form_graduacao.cleaned_data['agencia'],
                iniciacao_cientifica = form_graduacao.cleaned_data['iniciacao_cientifica'],
                residencia = novo_residencia
            )
            
            novo_endereco_trabalho = Endereco.objects.create(
                cep = form_endereco_trabalho.cleaned_data['cep'],
                endereco = form_endereco_trabalho.cleaned_data['endereco'],
                municipio = form_endereco_trabalho.cleaned_data['municipio'],
                uf = form_endereco_trabalho.cleaned_data['uf'],
                telefone1 = form_endereco_trabalho.cleaned_data['telefone1'],
                telefone2 = form_endereco_trabalho.cleaned_data['telefone2'],
            )
            novo_trabalho = Trabalho.objects.create(
                trabalho = form_trabalho.cleaned_data['trabalho'],
                endereco = novo_endereco_trabalho,
                email = form_trabalho.cleaned_data['email'],
                data_termino = form_trabalho.cleaned_data['data_termino'],
            )
            novo_endereco = Endereco.objects.create(
                cep = form_endereco.cleaned_data['cep'],
                endereco = form_endereco.cleaned_data['endereco'],
                municipio = form_endereco.cleaned_data['municipio'],
                uf = form_endereco.cleaned_data['uf'],
                telefone1 = form_endereco.cleaned_data['telefone1'],
                telefone2 = form_endereco.cleaned_data['telefone2'],
            )
            novo_aluno = Aluno.objects.create(
                nome = form_aluno.cleaned_data['nome'],
                cpf = form_aluno.cleaned_data['cpf'],
                nome_pai = form_aluno.cleaned_data['nome_pai'],
                nome_mae = form_aluno.cleaned_data['nome_mae'],
                naturalidade = form_aluno.cleaned_data['naturalidade'],
                nacionalidade = form_aluno.cleaned_data['nacionalidade'],
                dt_nascimento = form_aluno.cleaned_data['dt_nascimento'],
                estado_civil = form_aluno.cleaned_data['estado_civil'],
                identidade = form_aluno.cleaned_data['identidade'],
                identidade_uf = form_aluno.cleaned_data['identidade_uf'],
                identidade_orgao = form_aluno.cleaned_data['identidade_orgao'],
                sexo = form_aluno.cleaned_data['sexo'],
                email = form_aluno.cleaned_data['email'],
                etnia = form_aluno.cleaned_data['etnia'],
                cadastrado_por = request.user,
                endereco = novo_endereco,
                graduacao = novo_graduacao,
                titulacao = novo_titulacao,
                trabalho = novo_trabalho,
            )

            novo_ensino_medio.save()
            novo_titulacao.save()
            novo_residencia.save()
            novo_graduacao.save()
            novo_endereco_trabalho.save()
            novo_endereco.save()
            novo_trabalho.save()
            novo_aluno.save()

    return render(request, "cadastra_aluno.html", {'form_aluno':form_aluno, 'form_endereco':form_endereco, 'form_graduacao':form_graduacao, 'form_ensino_medio': form_ensino_medio, 'form_trabalho':form_trabalho, 'form_endereco_trabalho':form_endereco_trabalho, 'form_residencia':form_residencia, 'form_titulacao':form_titulacao})

def lista_aluno(request):
    alunos = Aluno.objects.all().order_by('nome')
    total = alunos.count()

    busca = request.GET.get('search')
    if busca:
        aluno_lists = Aluno.objects.filter(Q(nome__icontains = busca)| Q(cpf__icontains = busca))
        paginator = Paginator(aluno_lists, 15)
        page = request.GET.get('page')
        alunos = paginator.get_page(page)    

    return render(request, 'lista_aluno.html' , {'alunos': alunos, 'busca': busca, 'total':total})


