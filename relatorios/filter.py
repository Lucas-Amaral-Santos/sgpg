import django_filters
from django import forms
from aluno.models import Aluno
from matricula.models import Matricula
from config.models import Sexo, EstadoCivil, Etnia

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


    PROBATORIO_CHOICES = ((True,'Sim'),(False,'Não'))


    
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    probatorio__aluno__sexo = django_filters.ChoiceFilter(choices=[], label="Sexo:")
    probatorio__aluno__estado_civil = django_filters.ChoiceFilter(choices=[], label="Estado Civil:")
    probatorio__aluno__etnia = django_filters.ChoiceFilter(choices=[], label="Etnia:")
    probatorio__probatorio = django_filters.ChoiceFilter(label="Probatório:", choices=PROBATORIO_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['probatorio__aluno__sexo'].extra['choices'] = [(sexo.id, sexo) for sexo in Sexo.objects.all()]
        self.filters['probatorio__aluno__estado_civil'].extra['choices'] = [(estado_civil.id, estado_civil) for estado_civil in EstadoCivil.objects.all()]
        self.filters['probatorio__aluno__etnia'].extra['choices'] = [(etnia.id, etnia) for etnia in Etnia.objects.all()]

    class Meta:
        models = Matricula
        fields = ['status', 'probatorio__aluno__sexo', 'probatorio__aluno__estado_civil', 'probatorio__aluno__etnia', 'probatorio__probatorio']