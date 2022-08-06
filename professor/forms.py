from pyexpat import model
from django.forms import ModelForm
from .models import Professor, Trabalho, PosDoutorado


class PosDoutoradoForm(ModelForm):
    class Meta:
        model = PosDoutorado
        fields = '__all__'

class TrabalhoForm(ModelForm):
    class Meta:
        model = Trabalho
        fields = "__all__"

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"
        exclude = ['endereco', 'titulacao', 'graduacao', 'trabalho', 'pos_doutorado', 'slug', 'updated', 'cadastrado_por']