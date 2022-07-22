from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'uf', 'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade',
                  'identidade_uf', 'identidade_orgao', 'sexo', 'email']
