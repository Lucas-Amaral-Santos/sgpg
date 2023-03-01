from django.shortcuts import render

from matricula.models import Matricula
from .filter import MatriculaFilter
from config.models import Sexo, EstadoCivil, Etnia, StatusOptions
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


# Create your views here.
def filtra_aluno(request):    
    # f = AlunoFilter(request.GET, queryset=Aluno.objects.all())
    f = MatriculaFilter(request.GET, queryset=Matricula.objects.all())
    print(request.GET)
    grafico_sexo = f.qs.values("probatorio__aluno__sexo__sexo").annotate(nviews=Count('probatorio__aluno__sexo'))
    for i in grafico_sexo:
        i['cor'] = Sexo.objects.get(sexo=i['probatorio__aluno__sexo__sexo']).cor
         

    grafico_estado_civil = f.qs.values("probatorio__aluno__estado_civil__estado_civil").annotate(nviews=Count('probatorio__aluno__estado_civil'))
    for i in grafico_estado_civil:
        i['cor'] = EstadoCivil.objects.get(estado_civil=i['probatorio__aluno__estado_civil__estado_civil']).cor

    grafico_etnia = f.qs.values("probatorio__aluno__etnia__etnia").annotate(nviews=Count('probatorio__aluno__etnia'))
    for i in grafico_etnia:
        i['cor'] = Etnia.objects.get(etnia=i['probatorio__aluno__etnia__etnia']).cor

    grafico_status = f.qs.values("probatorio__aluno__status__status__status_options").annotate(nviews=Count('probatorio__aluno__status'))
    for i in grafico_status:
        i['cor'] = StatusOptions.objects.get(status_options=i['probatorio__aluno__status__status__status_options']).cor

    print(grafico_status)

    paginator = Paginator(f.qs, 5)

    page = request.GET.get('page')
    try:
        response = paginator.get_page(page)
    except PageNotAnInteger:
        response = paginator.get_page(1)
    except EmptyPage:
        response = paginator.get_page(paginator.num_pages)

    return render(request, 'filtra.html', {'filter': f, 'alunos': response, 'grafico_sexo': grafico_sexo, 'grafico_estado_civil': grafico_estado_civil, 'grafico_etnia': grafico_etnia, 'grafico_status': grafico_status})