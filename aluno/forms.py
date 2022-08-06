from django.forms import ModelForm
from .models import Aluno, Graduacao, Endereco, Trabalho, Residencia, Titulacao

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'naturalidade', 'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade',
                 'identidade_uf', 'identidade_orgao', 'sexo', 'email']

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class GraduacaoForm(ModelForm):
    class Meta:
        model = Graduacao
        fields = '__all__'
        exclude = ['residencia']

class TrabalhoForm(ModelForm):
    class Meta:
        model = Trabalho
        fields = '__all__'
        exclude = ['endereco']

class ResidenciaForm(ModelForm):
    class Meta:
        model = Residencia
        fields = '__all__'

class TitulacaoForm(ModelForm):
    class Meta:
        model = Titulacao
        fields = '__all__'