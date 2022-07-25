from django.forms import ModelForm
from .models import Professor

class ProfForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sexo', 'dt_nascimento', 'nacionalidade', 'naturalidade', 'cpf', 'identidade', 'identidade_orgao',
                 'identidade_uf', 'CRM', 'Estado', 'Siape']