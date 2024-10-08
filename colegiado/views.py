from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from professor.models import Professor
from matricula.models import Matricula
from .models import Colegiado
from .filters import ColegiadoFilter

# Create your views here.

def detalhes_colegiado(request):
    if not request.GET:
        tempdict = request.GET.copy()
        tempdict['data_saida__isnull'] = ['true']
        request.GET = tempdict


    f = ColegiadoFilter(request.GET, queryset=Colegiado.objects.all())

    return render(request, 'lista_colegiado.html', {'filter':f, 'total': f.qs.count, 'pagina': 'Colegiado'})
