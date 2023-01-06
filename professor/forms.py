from pyexpat import model
from django.forms import ModelForm, ValidationError
from .models import Professor, Trabalho, PosDoutorado, Colegiado

class ColegiadoForm(ModelForm):

    class Meta:
        model = Colegiado
        fields = '__all__'

class PosDoutoradoForm(ModelForm):
    class Meta:
        model = PosDoutorado
        fields = '__all__'

class TrabalhoForm(ModelForm):
    class Meta:
        model = Trabalho
        fields = "__all__"

class ProfessorForm(ModelForm):

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