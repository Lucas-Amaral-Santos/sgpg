import django_filters
from .models import Colegiado

class ColegiadoFilter(django_filters.FilterSet):

    colegiado_data_entrada = django_filters.DateRangeFilter(label='Data de Entrada:')
    colegiado_data_saida = django_filters.DateRangeFilter(label='Data de Saída:')
    
    professor_membro__nome = django_filters.CharFilter(lookup_expr='icontains')
    matricula_membro__probatorio__aluno__nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Colegiado
        fields = ['colegiado_data_entrada', 'colegiado_data_saida', 'status_membro', 'professor_membro__nome']