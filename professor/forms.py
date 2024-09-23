from django.forms import ModelForm, ValidationError, DateField, NumberInput, TextInput, CharField
from .models import Professor, Trabalho, PosDoutorado, Graduacao, Doutorado


class PosDoutoradoForm(ModelForm):
    class Meta:
        model = PosDoutorado
        fields = '__all__'

class DoutoradoForm(ModelForm):
    class Meta:
        model = Doutorado
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
        exclude = ['endereco', 'doutorado', 'graduacao', 'trabalho', 'pos_doutorado', 'slug', 'updated', 'cadastrado_por', 'membro_colegiado']