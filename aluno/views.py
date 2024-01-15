from django.shortcuts import render, redirect
from matricula.models import Matricula, Probatorio
from .forms import AlunoForm, EnderecoForm, GraduacaoForm, TrabalhoForm, ResidenciaForm, TitulacaoForm, EnsinoMedioForm, EnderecoTrabalhoForm
from .models import Aluno, Endereco, Graduacao, Trabalho, Residencia, Titulacao, EnsinoMedio, Status
from matricula.models import Probatorio
from matricula.forms import AlunoProbatorioForm
from config.models import StatusOptions
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
from django.contrib import messages
from faker import Factory

# Create your views here.

def cadastra_aluno(request, aluno=None):
    pagina = "Cadastrar Aluno"

    form_aluno = AlunoForm()
    form_endereco = EnderecoForm()
    form_graduacao = GraduacaoForm()
    form_ensino_medio = EnsinoMedioForm()
    form_trabalho = TrabalhoForm(prefix="trabalho")
    form_endereco_trabalho = EnderecoTrabalhoForm(prefix="trabalho")
    form_residencia = ResidenciaForm(initial={'residencia_ano_inicio': datetime.today().year, 'residencia_ano_fim': datetime.today().year})
    form_titulacao = TitulacaoForm()
    form_probatorio = AlunoProbatorioForm(initial={'data_inscricao': datetime.today().strftime(format="%d-%m-%Y")})

    if(aluno is not None):
        pagina = "Atualizar Aluno"
        aluno = Aluno.objects.get(slug=aluno)
        form_aluno = AlunoForm(instance=aluno)
        form_endereco = EnderecoForm(instance=aluno.endereco)
        form_graduacao = GraduacaoForm(instance=aluno.graduacao)
        form_ensino_medio = EnsinoMedioForm(instance=aluno.ensino_medio)
        form_trabalho = TrabalhoForm(instance=aluno.trabalho, prefix="trabalho")
        form_endereco_trabalho = EnderecoTrabalhoForm(instance=aluno.trabalho.endereco, prefix="trabalho")
        form_residencia = ResidenciaForm(instance=aluno.residencia)
        form_titulacao = TitulacaoForm(instance=aluno.titulacao)
        form_probatorio = AlunoProbatorioForm(instance=Probatorio.objects.get(aluno=aluno.slug))

        if request.method == "POST" and pagina == 'Atualizar Aluno':
            form_aluno = AlunoForm(request.POST, instance=aluno)
            form_endereco = EnderecoForm(request.POST, instance=aluno.endereco)
            form_graduacao = GraduacaoForm(request.POST, instance=aluno.graduacao)
            form_ensino_medio = EnsinoMedioForm(request.POST, instance=aluno.ensino_medio)
            form_trabalho = TrabalhoForm(request.POST, instance=aluno.trabalho, prefix="trabalho")
            form_endereco_trabalho = EnderecoTrabalhoForm(request.POST, instance=aluno.trabalho.endereco, prefix="trabalho")
            form_residencia = ResidenciaForm(request.POST, instance=aluno.residencia)
            form_titulacao = TitulacaoForm(request.POST, instance=aluno.titulacao)  
            form_probatorio = AlunoProbatorioForm(request.POST, instance=Probatorio.objects.get(aluno=aluno.slug))      

            if form_aluno.is_valid() and \
                form_endereco.is_valid() and \
                form_graduacao.is_valid() and \
                form_trabalho.is_valid() and \
                form_endereco_trabalho.is_valid() and \
                form_residencia.is_valid() and \
                form_titulacao.is_valid() and \
                form_ensino_medio.is_valid() and \
                form_probatorio.is_valid():

                form_aluno.save()
                form_endereco.save()
                form_graduacao.save()
                form_ensino_medio.save()
                form_trabalho.save()
                form_endereco_trabalho.save()
                form_residencia.save()
                form_titulacao.save()
                form_probatorio.save()

                messages.success(request, 'Aluno atualizado com sucesso!')
                return redirect('aluno:detalhes_aluno', aluno=aluno.slug)

    if request.method == "POST":
        form_aluno = AlunoForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        form_graduacao = GraduacaoForm(request.POST)
        form_ensino_medio = EnsinoMedioForm(request.POST)
        form_trabalho = TrabalhoForm(request.POST, prefix="trabalho")
        form_endereco_trabalho = EnderecoTrabalhoForm(request.POST, prefix="trabalho")
        form_residencia = ResidenciaForm(request.POST)
        form_titulacao = TitulacaoForm(request.POST)
        form_probatorio = AlunoProbatorioForm(request.POST)

        if form_aluno.is_valid() and \
            form_endereco.is_valid() and \
            form_graduacao.is_valid() and \
            form_trabalho.is_valid() and \
            form_endereco_trabalho.is_valid() and \
            form_residencia.is_valid() and \
            form_titulacao.is_valid() and \
            form_ensino_medio.is_valid() and \
            form_probatorio.is_valid():

            status_opcao = None
            novo_status = None

            try:
                status_opcao = StatusOptions.objects.get(status_options='Probatório')
            except:
                StatusOptions.objects.create(status_options='Probatório', cor=Factory.create().hex_color()).save()
                status_opcao = StatusOptions.objects.get(status_options='Probatório')

            novo_status = Status.objects.create(
                status = status_opcao
            )
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
                portador_deficiencia = form_aluno.cleaned_data['portador_deficiencia'],
                portador_deficiencia_qual = form_aluno.cleaned_data['portador_deficiencia_qual'],
                foto = form_aluno.cleaned_data['foto'],
                status = novo_status,
                cadastrado_por = request.user,
                endereco = novo_endereco,
                graduacao = novo_graduacao,
                titulacao = novo_titulacao,
                trabalho = novo_trabalho,
                residencia = novo_residencia,
                ensino_medio = novo_ensino_medio,
            )

            novo_probatorio = Probatorio.objects.create(
                data_inscricao = form_probatorio.cleaned_data['data_inscricao'],
                aluno = novo_aluno,
                grau = form_probatorio.cleaned_data['grau'],
                cadastrado_por = request.user,
            )

            novo_ensino_medio.save()
            novo_titulacao.save()
            novo_residencia.save()
            novo_graduacao.save()
            novo_endereco_trabalho.save()
            novo_endereco.save()
            novo_trabalho.save()
            novo_aluno.save()
            novo_probatorio.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('aluno:detalhes_aluno', aluno=novo_aluno.slug)
        
        print(form_graduacao.errors)
        return render(request, "cadastra_aluno.html", {'pagina': pagina, 'form_aluno':form_aluno, 'form_endereco':form_endereco, 
                                                       'form_graduacao':form_graduacao, 'form_ensino_medio': form_ensino_medio, 
                                                       'form_trabalho':form_trabalho, 'form_endereco_trabalho': form_endereco_trabalho, 
                                                       'form_residencia':form_residencia, 'form_titulacao':form_titulacao, 
                                                       'form_probatorio': form_probatorio, 'aluno': aluno})        

    return render(request, "cadastra_aluno.html", {'pagina': pagina, 'form_aluno':form_aluno, 'form_endereco':form_endereco, 'form_graduacao':form_graduacao, 'form_ensino_medio': form_ensino_medio, 'form_trabalho':form_trabalho, 'form_endereco_trabalho': form_endereco_trabalho, 'form_residencia':form_residencia, 'form_titulacao':form_titulacao, 'form_probatorio': form_probatorio, 'aluno': aluno})

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

def detalhes_aluno(request, aluno):
    aluno = Aluno.objects.get(slug=aluno)
    probatorio = None
    matricula = None
    try:
        probatorio = Probatorio.objects.get(aluno=aluno)
    except:
        probatorio = None
    

    if probatorio is not None:
        try:
            matricula = Matricula.objects.get(probatorio = probatorio)
        except:
            matricula = None
    return render(request, 'detalhes_aluno.html', {'aluno': aluno, 'probatorio': probatorio, 'matricula': matricula})


def delete_aluno(request, aluno):
    aluno = Aluno.objects.get(slug=aluno)
    aluno.delete()
    messages.success(request, 'Aluno apagado do sistema!')
    return redirect('aluno:lista_aluno')