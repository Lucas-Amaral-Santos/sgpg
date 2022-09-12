import django_filters
from aluno.models import Aluno

class AlunoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    cpf = django_filters.CharFilter(lookup_expr='icontains')
    nome_pai = django_filters.CharFilter(lookup_expr='icontains')



    class Meta:
        models = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'naturalidade', 'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade', 'identidade_uf', 'identidade_orgao', 'sexo', 'email', 'raca', 'etnia']