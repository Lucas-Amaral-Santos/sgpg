from django.forms import ModelForm, CharField, TextInput, DateField, NumberInput, ChoiceField, ValidationError
from .models import Aluno, Graduacao, Endereco, Trabalho, Residencia, Titulacao, Afastamento, EnsinoMedio

class AlunoForm(ModelForm):
    dt_nascimento = DateField(label="Data de Nascimento:", widget=NumberInput(attrs={'type':'date'}))
    cpf = CharField(max_length="14", label="CPF:", required=False, widget=TextInput(attrs={"data-mask": "000.000.000-00"}))

    def clean_portador_deficiencia_qual(self):
        cleaned_data = self.cleaned_data

        portador_deficiencia_qual = cleaned_data.get("portador_deficiencia_qual")

        if not portador_deficiencia_qual and cleaned_data.get("portador_deficiencia"):
            raise ValidationError('Especifique a deficiência.')

        return cleaned_data['portador_deficiencia_qual']
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'naturalidade', 
                  'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade',
                 'identidade_uf', 'identidade_orgao', 'sexo', 'email', 'etnia',
                 'portador_deficiencia','portador_deficiencia_qual', 'foto']

class EnderecoForm(ModelForm):
    cep = CharField(label="CEP:", required=False, widget=TextInput(attrs={"data-mask": "00000-000"}))
    endereco = CharField(label="Rua:", required=False, widget=TextInput(attrs={"id": "id_rua"}))
    telefone1 = CharField(label="Telefone:", required=False, widget=TextInput(attrs={"data-mask": "(00) 00000-0000"}))
    telefone2 = CharField(label="Telefone 2:", required=False, widget=TextInput(attrs={"data-mask": "(00) 00000-0000"}))

    class Meta:
        model = Endereco
        fields = '__all__'

class EnderecoTrabalhoForm(ModelForm):
    cep = CharField(label="CEP: ", required=False, widget=TextInput(attrs={"data-mask": "00000-000", "id": "id_trabalho_cep", "name": "trabalho_cep"}))
    endereco = CharField(label="Rua: ", required=False, widget=TextInput(attrs={"id": "id_trabalho_rua", "name": "trabalho_rua"}))
    numero = CharField(label = "Número: ", required=False, widget=NumberInput(attrs={"id": "id_trabalho_numero", "name": "trabalho_numero"}))
    complemento = CharField(label = "Complemento: ", required=False, widget=TextInput(attrs={"id": "id_trabalho_complemento", "name": "trabalho_complemento"}))
    bairro = CharField(label = "Bairro: ", required=False, widget=TextInput(attrs={"id": "id_trabalho_bairro", "name": "trabalho_bairro"}))
    municipio = CharField(label = "Município: ", required=False, widget=TextInput(attrs={"id": "id_trabalho_municipio", "name": "trabalho_municipio"}))
    uf = CharField(label = "UF: ", required=False, widget=TextInput(attrs={"id": "id_trabalho_uf", "name": "trabalho_uf"}))
    pais = CharField(label = "País: ", required=False, widget=TextInput(attrs={"id": "id_trabalho_pais", "name": "trabalho_pais"}))
    telefone1 = CharField(label="Telefone:", required=False, widget=TextInput(attrs={"data-mask": "(00) 00000-0000", "id": "id_trabalho_telefone", "name": "trabalho_telefone"}))
    telefone2 = CharField(label="Telefone 2:", required=False, widget=TextInput(attrs={"data-mask": "(00) 00000-0000", "id": "id_trabalho_telefone2", "name": "trabalho_telefone2"}))

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
    data_qualificacao = DateField(required=False, label="Data da Qualificação:", widget=NumberInput(attrs={'type':'date'}))
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