from django.forms import ModelForm, ValidationError, DateField, NumberInput, TextInput
from .models import Professor, Trabalho, PosDoutorado, Colegiado
from datetime import datetime

class ColegiadoForm(ModelForm):
    colegiado_data_entrada = DateField(required=False, widget=TextInput(attrs={'type':'date'}))
    colegiado_data_saida = DateField(required=False, widget=TextInput(attrs={'type':'date'}), initial=datetime.today().strftime('%d/%m/%Y'))
    class Meta:
        model = Colegiado
        fields = '__all__'

class PosDoutoradoForm(ModelForm):
    class Meta:
        model = PosDoutorado
        fields = '__all__'

class TrabalhoForm(ModelForm):
    admissao = DateField(required=False, widget=TextInput(attrs={'type':'date'}))
    class Meta:
        model = Trabalho
        fields = "__all__"

class ProfessorForm(ModelForm):
    dt_nascimento = DateField(required=False, widget=TextInput(attrs={'type':'date'}))

    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data

        estrangeiro = cleaned_data.get("estrangeiro")
        cpf = cleaned_data.get("cpf")

        if not cpf and not estrangeiro:
            raise ValidationError('Informar CPF.')


        return cleaned_data

    class Meta:
        model = Professor
        fields = "__all__"
        exclude = ['endereco', 'titulacao', 'graduacao', 'trabalho', 'pos_doutorado', 'slug', 'updated', 'cadastrado_por', 'membro_colegiado']