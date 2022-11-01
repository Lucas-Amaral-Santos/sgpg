import django_filters
from aluno.models import Aluno
from matricula.models import Matricula

class AlunoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    cpf = django_filters.CharFilter(lookup_expr='icontains')
    nome_pai = django_filters.CharFilter(lookup_expr='icontains')



    class Meta:
        models = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'naturalidade', 'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade', 'identidade_uf', 'identidade_orgao', 'sexo', 'email', 'raca', 'etnia']



class MatriculaFilter(django_filters.FilterSet):
    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Titulado', 'Titulado'),
        ('Jubilado', 'Jubilado'),
        ('Abandono', 'Abandono')
    )

    SEXO_CHOICES = (
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
    )

    
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    probatorio__aluno__sexo = django_filters.ChoiceFilter(choices=SEXO_CHOICES)
    class Meta:
        models = Matricula
        fields = ['status', 'probatorio__aluno__sexo']