from django.forms import ModelForm, CharField, TextInput, DateField, NumberInput, ChoiceField
from .models import Aluno, Graduacao, Endereco, Trabalho, Residencia, Titulacao, Afastamento, EnsinoMedio

class AlunoForm(ModelForm):
    dt_nascimento = DateField(label="Data de Nascimento:", widget=NumberInput(attrs={'type':'date'}))
    cpf = CharField(max_length="14", label="CPF:", required=False, widget=TextInput(attrs={"data-mask": "000.000.000-00"}))
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'naturalidade', 
                  'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade',
                 'identidade_uf', 'identidade_orgao', 'sexo', 'email', 'etnia']

class EnderecoForm(ModelForm):
    telefone1 = CharField(label="Telefone:", required=False, widget=TextInput(attrs={"data-mask": "(00) 00000-0000"}))
    telefone2 = CharField(label="Telefone 2:", required=False, widget=TextInput(attrs={"data-mask": "(00) 00000-0000"}))

    class Meta:
        model = Endereco
        fields = '__all__'

class GraduacaoForm(ModelForm):
    class Meta:
        model = Graduacao
        fields = '__all__'
        exclude = ['residencia']

class EnsinoMedioForm(ModelForm):
    class Meta:
        model = EnsinoMedio
        fields = '__all__'

class TrabalhoForm(ModelForm):
    data_termino = DateField(widget=NumberInput(attrs={'type':'date'}), required=False, label="Data de Término:")
    class Meta:
        model = Trabalho
        fields = '__all__'
        exclude = ['endereco']

class ResidenciaForm(ModelForm):
    class Meta:
        model = Residencia
        fields = '__all__'

class TitulacaoForm(ModelForm):
    data_qualificacao = DateField(label="Data da Qualificação:", widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Titulacao
        fields = '__all__'

class TitulacaoProfessorForm(ModelForm):
    class Meta:
        model = Titulacao
        fields = '__all__'
        exclude = ['data_qualificacao']

class AfastamentoForm(ModelForm):
    class Meta:
        model = Afastamento
        fields = '__all__'