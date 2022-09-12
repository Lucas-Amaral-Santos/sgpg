from django.shortcuts import render
from .filter import AlunoFilter
from aluno.models import Aluno
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def filtra_aluno(request):

    f = AlunoFilter(request.GET, queryset=Aluno.objects.all())
    paginator = Paginator(f.qs, 5)

    page = request.GET.get('page')
    try:
        response = paginator.get_page(page)
    except PageNotAnInteger:
        response = paginator.get_page(1)
    except EmptyPage:
        response = paginator.get_page(paginator.num_pages)

    return render(request, 'filtra.html', {'filter': f, 'alunos': response})