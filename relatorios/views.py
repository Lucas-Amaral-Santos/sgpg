from django.shortcuts import render

from matricula.models import Matricula, Probatorio
from aluno.models import Aluno
from .filter import MatriculaFilter, AlunoFilter, ProbatorioFilter
from config.models import Sexo, EstadoCivil, Etnia, StatusOptions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from faker import Factory



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

    paginator = Paginator(f.qs, 5)

    page = request.GET.get('page')
    try:
        response = paginator.get_page(page)
    except PageNotAnInteger:
        response = paginator.get_page(1)
    except EmptyPage:
        response = paginator.get_page(paginator.num_pages)

    return render(request, 'filtra.html', {'filter': f, 'alunos': response, 'grafico_sexo': grafico_sexo, 'grafico_estado_civil': grafico_estado_civil, 'grafico_etnia': grafico_etnia, 'grafico_status': grafico_status})