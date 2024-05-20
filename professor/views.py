from django.shortcuts import render, redirect
from .forms import ProfessorForm, TrabalhoForm, PosDoutoradoForm, ColegiadoForm, GraduacaoForm, DoutoradoForm
from  .models import Professor, Trabalho, PosDoutorado, Colegiado, Graduacao, Doutorado
from django.contrib.auth.models import User

from aluno.models import Endereco
from aluno.forms import EnderecoForm, TitulacaoProfessorForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

def cadastra_professor(request, professor=None):
    pagina = "Cadastrar Professor"
    form_professor = ProfessorForm()
    form_graduacao = GraduacaoForm()
    form_trabalho = TrabalhoForm()
    form_pos_doutorado = PosDoutoradoForm()
    form_endereco = EnderecoForm()
    form_doutorado = DoutoradoForm()

    if (professor is not None):
        pagina = "Atualizar Professor"
        professor = Professor.objects.get(slug=professor)
        form_professor = ProfessorForm(instance=professor)
        form_graduacao = GraduacaoForm(instance=professor.graduacao)
        form_trabalho = TrabalhoForm(instance=professor.trabalho)
        form_pos_doutorado = PosDoutoradoForm(instance=professor.pos_doutorado)
        form_endereco = EnderecoForm(instance=professor.endereco)
        form_doutorado = DoutoradoForm(instance=professor.doutorado)

        if request.method == "POST" and pagina == 'Atualizar Professor':
            form_professor = ProfessorForm(request.POST, instance=professor)
            form_graduacao = GraduacaoForm(request.POST, instance=professor.graduacao)
            form_trabalho = TrabalhoForm(request.POST, instance=professor.trabalho)
            form_pos_doutorado = PosDoutoradoForm(request.POST, instance=professor.pos_doutorado)
            form_endereco = EnderecoForm(request.POST, instance=professor.endereco)
            form_doutorado = DoutoradoForm(request.POST, instance=professor.doutorado)

            if form_professor.is_valid()  and \
                form_graduacao.is_valid() and form_trabalho.is_valid() and \
                form_pos_doutorado.is_valid() and form_endereco.is_valid() and \
                form_doutorado.is_valid():

                form_professor.save()
                form_graduacao.save()
                form_trabalho.save()
                form_pos_doutorado.save()
                form_endereco.save()
                form_doutorado.save()

                messages.success(request, 'Professor atualizado com sucesso!')
                return redirect('professor:detalhes_professor', professor=professor.slug)
        
    if request.method == "POST":
        form_professor = ProfessorForm(request.POST)
        form_graduacao = GraduacaoForm(request.POST)
        form_trabalho = TrabalhoForm(request.POST)
        form_pos_doutorado = PosDoutoradoForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        form_doutorado = DoutoradoForm(request.POST)

        if form_professor.is_valid()  and \
            form_graduacao.is_valid() and form_trabalho.is_valid() and \
            form_pos_doutorado.is_valid() and form_doutorado.is_valid() and \
            form_endereco.is_valid():
            

            novo_doutorado = Doutorado.objects.create(
                doutorado = form_doutorado.cleaned_data['doutorado'],
                doutorado_area = form_doutorado.cleaned_data['doutorado_area'],
                doutorado_ano = form_doutorado.cleaned_data['doutorado_ano'],
                uf = form_doutorado.cleaned_data['uf'],
                instituicao_doutorado = form_doutorado.cleaned_data['instituicao_doutorado'],
                obs_geral = form_doutorado.cleaned_data['obs_geral'],
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
                pos_doutorado =  form_pos_doutorado.cleaned_data['pos_doutorado'],
                # ano_inicio = form_pos_doutorado.cleaned_data['ano_inicio'],
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

            nova_graduacao = Graduacao.objects.create(
                graduacao_area = form_graduacao.cleaned_data['graduacao_area'],
                instituicao = form_graduacao.cleaned_data['instituicao'],
                local = form_graduacao.cleaned_data['local'],
                graduacao_ano_inicio = form_graduacao.cleaned_data['graduacao_ano_inicio'],
                graduacao_ano_fim = form_graduacao.cleaned_data['graduacao_ano_fim'],
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
                graduacao = nova_graduacao,
                pos_doutorado = novo_pos_doutorado,
                doutorado = novo_doutorado,
                endereco = novo_endereco,
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            novo_doutorado.save()
            novo_endereco.save()
            novo_pos_doutorado.save()
            novo_trabalho.save()
            nova_graduacao.save()
            novo_professor.save()

            messages.success(request, 'Professor cadastrado com sucesso!')            
            return redirect('professor:detalhes_professor', professor=novo_professor.slug)
        
        return render(request, "cadastra_professor.html", {'form_professor': form_professor, 'form_graduacao': form_graduacao, 'form_trabalho': form_trabalho, 'form_pos_doutorado':form_pos_doutorado, 'form_endereco': form_endereco, 'form_doutorado': form_doutorado, 'pagina':pagina})
    
    return render(request, "cadastra_professor.html", {'form_professor': form_professor, 'form_graduacao': form_graduacao, 'form_trabalho': form_trabalho, 'form_pos_doutorado':form_pos_doutorado, 'form_endereco': form_endereco, 'form_doutorado': form_doutorado, 'pagina':'Cadastrar Professor'})

def lista_professor(request):
    professores = Professor.objects.all().order_by('nome')
    total = professores.count()

    busca = request.GET.get('search')
    if busca:
        professor_lists = Professor.objects.filter(Q(nome__icontains = busca)| Q(cpf__icontains = busca))
        paginator = Paginator(professor_lists, 15)
        page = request.GET.get('page')
        professores = paginator.get_page(page)  

    return render(request, 'lista_professor.html' , {'professores': professores, 'pagina': 'Pesquisar Professor', 'busca': busca, 'total':total})

def detalhes_professor(request, professor):

    professor = Professor.objects.get(slug=professor)
    colegiados = professor.membro_colegiado.all()
    form_colegiado = ColegiadoForm()

    if request.method == 'POST':
        form_colegiado = ColegiadoForm(request.POST)
        if form_colegiado.is_valid():
            novo_colegiado = Colegiado.objects.create(
                colegiado_data_entrada = form_colegiado.cleaned_data['colegiado_data_entrada'],
                colegiado_data_saida = form_colegiado.cleaned_data['colegiado_data_saida'],
                status_membro = form_colegiado.cleaned_data['status_membro']
            )
            novo_colegiado.save()
            novo_colegiado.professor_set.add(professor)
            messages.success(request, 'Colegiado atualizado com sucesso!')
            return redirect('professor:detalhes_professor', professor=professor.slug)

    return render(request, 'detalhes_professor.html', {'professor':professor, 'colegiados':colegiados, 'form_colegiado':form_colegiado, 'pagina': 'Detalhes Professor'})

def detalhes_colegiado(request, membros_ativos=True):
    colegiado = Professor.objects.filter(membro_colegiado__colegiado_membro=True)
    total = colegiado.count()

    data_entrada_inicio = request.GET.get('data_entrada_inicio')
    data_entrada_fim = request.GET.get('data_entrada_fim')
    data_saida_inicio = request.GET.get('data_saida_inicio')
    data_saida_fim = request.GET.get('data_saida_fim')
    membros_ativos = request.GET.get('membros_ativos')
    membros_anteriores = request.GET.get('membros_passados')    
    busca = request.GET.get('search')

    if membros_ativos:
        colegiado = Professor.objects.filter(membro_colegiado__colegiado_membro=False)

    # Utiliza o método GET para fazer os filtros no intervalo das datas de entrada do professor como membro do colegiado
    if data_entrada_inicio and not data_entrada_fim:
        colegiado = colegiado.filter(membro_colegiado__colegiado_data_entrada__lte=data_entrada_inicio)
    elif not data_entrada_inicio and data_entrada_fim:
        colegiado = colegiado.filter(membro_colegiado__colegiado_data_entrada__lte=data_entrada_fim)
    elif data_entrada_inicio and data_entrada_fim:
        colegiado = colegiado.filter(membro_colegiado__colegiado_data_entrada__range=[data_entrada_inicio, data_entrada_fim])
    
    # Utiliza o método GET para fazer os filtros no intervalo das datas de saída do professor como membro do colegiado
    if membros_anteriores:
        if data_saida_inicio and not data_saida_fim:
            colegiado = colegiado.filter(membro_colegiado__colegiado_data_saida__lte=data_saida_inicio)
        elif not data_saida_inicio and data_saida_fim:
            colegiado = colegiado.filter(membro_colegiado__colegiado_data_saida__lte=data_saida_fim)
        elif data_saida_inicio and data_saida_fim:
            colegiado = colegiado.filter(membro_colegiado__colegiado_data_saida__range=[data_saida_inicio, data_saida_fim])

    if busca:
        professor_lists = colegiado.filter(Q(nome__icontains = busca)| Q(cpf__icontains = busca))
        paginator = Paginator(professor_lists, 15)
        page = request.GET.get('page')
        colegiado = paginator.get_page(page)  

    return render(request, 'lista_professor.html', {'professores':colegiado, 'pagina': 'Colegiado', 'total':total, 'busca': busca})

def delete_professor(request, professor):
    professor = Professor.objects.get(slug=professor)
    professor.delete()
    messages.success(request, 'Professor apagado do sistema!')
    return redirect('professor:lista_professor')