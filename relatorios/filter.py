import django_filters
from django import forms
from aluno.models import Aluno
from matricula.models import Matricula
from config.models import Sexo, EstadoCivil, Etnia, StatusOptions

class AlunoFilter(django_filters.FilterSet):
    # nome = django_filters.CharFilter(lookup_expr='icontains')
    # cpf = django_filters.CharFilter(lookup_expr='icontains')
    # nome_pai = django_filters.CharFilter(lookup_expr='icontains')
    status__status = django_filters.ChoiceFilter(choices=[], label="Status:")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['status__status'].extra['choices'] = [(status.id, status) for status in StatusOptions.objects.all()]

    class Meta:
        models = Aluno
        fields = ['status__status']


class MatriculaFilter(django_filters.FilterSet):

    probatorio__aluno__sexo = django_filters.ChoiceFilter(choices=[], label="Sexo:")
    probatorio__aluno__estado_civil = django_filters.ChoiceFilter(choices=[], label="Estado Civil:")
    probatorio__aluno__etnia = django_filters.ChoiceFilter(choices=[], label="Etnia:")
    probatorio__aluno__status__status = django_filters.ChoiceFilter(label="Status:", choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['probatorio__aluno__sexo'].extra['choices'] = [(sexo.id, sexo) for sexo in Sexo.objects.all()]
        self.filters['probatorio__aluno__estado_civil'].extra['choices'] = [(estado_civil.id, estado_civil) for estado_civil in EstadoCivil.objects.all()]
        self.filters['probatorio__aluno__etnia'].extra['choices'] = [(etnia.id, etnia) for etnia in Etnia.objects.all()]
        self.filters['probatorio__aluno__status__status'].extra['choices'] = [(status.id, status) for status in StatusOptions.objects.all()]

    class Meta:
        models = Matricula
        fields = ['probatorio__aluno__sexo', 'probatorio__aluno__estado_civil', 'probatorio__aluno__etnia', 'probatorio__probatorio', 'probatorio__aluno__status__status']