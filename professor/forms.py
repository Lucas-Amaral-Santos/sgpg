from django.forms import ModelForm, ValidationError, DateField, NumberInput, TextInput, CharField
from .models import Professor, Trabalho, PosDoutorado, Colegiado, Graduacao
from datetime import datetime

class ColegiadoForm(ModelForm):
    colegiado_data_entrada = DateField(label='Data de entrada:', required=False, widget=TextInput(attrs={'type':'date'}))
    colegiado_data_saida = DateField(label='Data de término:', required=False, widget=TextInput(attrs={'type':'date'}), initial=datetime.today().strftime('%d/%m/%Y'))
    class Meta:
        model = Colegiado
        fields = '__all__'

class PosDoutoradoForm(ModelForm):
    class Meta:
        model = PosDoutorado
        fields = '__all__'

class GraduacaoForm(ModelForm):
    class Meta:
        model = Graduacao
        fields = '__all__'

class TrabalhoForm(ModelForm):
    admissao = DateField(label='Admissão:', required=False, widget=TextInput(attrs={'type':'date'}))
    class Meta:
        model = Trabalho
        fields = "__all__"

class ProfessorForm(ModelForm):
    dt_nascimento = DateField(label='Data de Nascimento:', required=False, widget=TextInput(attrs={'type':'date'}))
    cpf = CharField(max_length="14", label="CPF:", required=False, widget=TextInput(attrs={"data-mask": "000.000.000-00"}))

    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)

    def clean_cpf(self):
        cleaned_data = self.cleaned_data

        cpf = cleaned_data.get("cpf")

        if not cpf and not cleaned_data.get("estrangeiro"):
            raise ValidationError('Informar CPF. Não necessário em caso de profesoor estrangeiro.')

        return cleaned_data['cpf']

    class Meta:
        model = Professor
        fields = "__all__"
        exclude = ['endereco', 'titulacao', 'graduacao', 'trabalho', 'pos_doutorado', 'slug', 'updated', 'cadastrado_por', 'membro_colegiado']