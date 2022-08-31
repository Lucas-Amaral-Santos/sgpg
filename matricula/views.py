from django.shortcuts import render, redirect
from .forms import MatriculaForm
from .models import Matricula
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
                aluno = form.cleaned_data['aluno'],
                cadastrado_por = User.objects.get(pk=request.user.id),
            )

            nova_matricula.save()

            return redirect('/')
    
    return render(request, 'cadastra_matricula.html', {'form':form})


def lista_matricula(request):
    matriculas = Matricula.objects.all().order_by('aluno')
    total = matriculas.count()

    busca = request.GET.get('search')
    if busca:
        matricula_lists = Matricula.objects.filter(Q(numero__icontains = busca)| Q(aluno__nome__icontains = busca))
        paginator = Paginator(matricula_lists, 15)
        page = request.GET.get('page')
        matriculas = paginator.get_page(page)    

    return render(request, 'lista_matricula.html' , {'matriculas': matriculas, 'busca': busca, 'total':total})

def detalhe_matricula(request, matricula):
    
    matricula = Matricula.objects.get(id=matricula)

    return render(request, 'detalhe_matricula.html', {'matricula':matricula}) 