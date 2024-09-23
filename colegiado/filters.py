import django_filters
from django.db.models import Q
from django.forms import CheckboxInput
from .models import Colegiado


class ColegiadoFilter(django_filters.FilterSet):

    colegiado_data_entrada = django_filters.DateRangeFilter(label='Data de Entrada:')
    colegiado_data_saida = django_filters.DateRangeFilter(label='Data de Saída:')

    pesquisar = django_filters.CharFilter(method='filter_by_all_name_fields', label='Pesquisar')
    data_saida__isnull = django_filters.BooleanFilter(field_name='colegiado_data_saida', lookup_expr='isnull', widget=CheckboxInput, label='Ativo')
    
    

    class Meta:
        model = Colegiado
        fields = ['colegiado_data_entrada', 'colegiado_data_saida', 'status_membro']
        
  
    def filter_by_all_name_fields(self, queryset, value):
        return queryset.filter(
            Q(professor_membro__nome__icontains=value) | Q(professor_membro__cpf__icontains=value) | Q(matricula_membro__probatorio__aluno__nome__icontains=value) | Q(matricula_membro__probatorio__aluno__cpf__icontains=value)
        )