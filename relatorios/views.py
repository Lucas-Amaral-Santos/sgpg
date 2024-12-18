from django.shortcuts import render
from matricula.models import Matricula, Probatorio
from aluno.models import Aluno
from .filter import MatriculaFilter, AlunoFilter, ProbatorioFilter
from config.models import Sexo, EstadoCivil, Etnia, StatusOptions, Grau
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from faker import Factory
from datetime import datetime
import csv
from io import BytesIO
from django.http import HttpResponse


# Create your views here.
def filtra_aluno(request):    
    f = AlunoFilter(request.GET, queryset=Aluno.objects.all())


    grafico_sexo = f.qs.values("sexo__sexo").annotate(nviews=Count('sexo')).filter(sexo__sexo__isnull=False)
    print(grafico_sexo)
    for i in grafico_sexo:  
            i['cor'] = Sexo.objects.get(sexo=i['sexo__sexo']).cor
         

    grafico_estado_civil = f.qs.values("estado_civil__estado_civil").annotate(nviews=Count('estado_civil')).filter(estado_civil__estado_civil__isnull=False)
    for i in grafico_estado_civil:
        i['cor'] = EstadoCivil.objects.get(estado_civil=i['estado_civil__estado_civil']).cor

    grafico_etnia = f.qs.values("etnia__etnia").annotate(nviews=Count('etnia'))
    for i in grafico_etnia:
        i['cor'] = Etnia.objects.get(etnia=i['etnia__etnia']).cor

    grafico_status = f.qs.values("status__status__status_options").annotate(nviews=Count('status')).filter(status__status__status_options__isnull=False)
    for i in grafico_status:
        i['cor'] = StatusOptions.objects.get(status_options=i['status__status__status_options']).cor


    grafico_grau = f.qs.values("probatorio_aluno__grau__grau").annotate(nviews=Count('probatorio_aluno__grau__grau'))
    for i in grafico_grau:
        i['cor'] = Grau.objects.get(grau=i['probatorio_aluno__grau__grau']).cor

    grafico_dt_nascimento = f.qs.values("dt_nascimento__year").annotate(nviews=Count('dt_nascimento'))

    grafico_dt_cadastro = f.qs.values("dt_cadastro__year").annotate(nviews=Count('dt_cadastro'))
    grafico_mestrado = f.qs.filter(probatorio_aluno__grau__grau='Mestrado').values("dt_cadastro__year").annotate(nviews=Count('dt_cadastro'))



    grafico_doutorado = f.qs.filter(probatorio_aluno__grau__grau='Doutorado').values("dt_cadastro__year").annotate(nviews=Count('dt_cadastro'))
    for i in grafico_doutorado:
        i['cor'] = Grau.objects.get(grau=i['probatorio_aluno__grau__grau']).cor



    # TODO GRAFICO DOS ALUNOS QUE ENTRARAM NOS ÚLTIMOS ANOS

    # curr_year = datetime.now().year
    # quadrienio = [curr_year, curr_year-1, curr_year-2, curr_year-3, curr_year-4, curr_year-5, curr_year-6]
    # num_mat = []
    # num_mest = []
    # num_doc = []
    # for years in quadrienio:
    #     num_mat += [Matricula.objects.filter(dt_cadastro__year = years).count()]
    #     num_mest += [Matricula.objects.filter(grau=1).filter(dt_cadastro__year = years).count()]
    #     num_doc += [Matricula.objects.filter(grau=2).filter(dt_cadastro__year = years).count()]


    paginator = Paginator(f.qs, 5)

    page = request.GET.get('page')
    try:
        response = paginator.get_page(page)
    except PageNotAnInteger:
        response = paginator.get_page(1)
    except EmptyPage:
        response = paginator.get_page(paginator.num_pages)

    if request.method == 'POST':
        print(str(request.POST.get('export')))
        if str(request.POST.get('export')) == 'csv' :
            return export_cliente_csv(request, f.qs)


    return render(request, 'filtra.html', {'filter': f, 'alunos': response, 'grafico_sexo': grafico_sexo, 'grafico_estado_civil': grafico_estado_civil, 'grafico_etnia': grafico_etnia, 'grafico_status': grafico_status, 'grafico_grau': grafico_grau, 'grafico_dt_nascimento': grafico_dt_nascimento, 'grafico_dt_cadastro': grafico_dt_cadastro, 'grafico_mestrado': grafico_mestrado, 'grafico_doutorado': grafico_doutorado})


def export_cliente_csv(request, clientes):
    
    # Get all data from cDetail Databse Table
    clientes = clientes.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="alunos.csv"'

    fields = ['Nome', 'CPF', 'Sexo', 'Pai', 'Mãe', 'Naturalidade', 'Nacionalidade', 'Data de Nasc', 'Estado Civil', 'Identidade', 'Id-UF', 'Id-Orgão', 'Sexo', 'Email', 'Etnia', 'Port. Deficiência', 'Qual Deficiência', 'Status', 'Probatório', 'Data da Inscrição', 'Linha de Pesquisa', 'Grau', 'Número', 'Curso', 'Requisita bolsa', 'Título TRabalho Final', 'Nota Trabalho Final', 'Entregue Versão Final', 'Data do Diploma', 'Diploma Entregue', 'Orientadores']
    writer = csv.writer(response)
    writer.writerow(fields)    

    for c in clientes:

        obj = [c.nome, c.cpf, c.sexo, c.nome_pai, c.nome_mae, c.naturalidade, c.nacionalidade, c.dt_nascimento, c.estado_civil, c.identidade, c.identidade_uf, c.identidade_orgao, c.sexo, c.email, c.etnia, c.portador_deficiencia, c.portador_deficiencia_qual, c.status, c.probatorio_aluno.probatorio, c.probatorio_aluno.data_inscricao, c.probatorio_aluno.linha_pesquisa, c.probatorio_aluno.grau]
        if(c.probatorio_aluno.matricula_probatorio.first() is not None):
            obj += [c.probatorio_aluno.matricula_probatorio.first().numero, c.probatorio_aluno.matricula_probatorio.first().curso, c.probatorio_aluno.matricula_probatorio.first().requisita_bolsa]
            if(c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final is not None):
                if(c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.orientacao_trabalho_final is not None):         
                    obj += [c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.titulo, c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.nota, c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.versao_final, c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.dt_diploma, c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.diploma]       
                    aux = ''
                    for o in c.probatorio_aluno.matricula_probatorio.first().matricula_trabalho_final.orientacao_trabalho_final.all():
                        aux += o.professor.nome + ' '
                        print(aux)
                obj += [aux]
                    
        writer.writerow(obj)

    return response