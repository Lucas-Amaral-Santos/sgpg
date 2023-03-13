from .models import UnidadeFederativa, Sexo, Etnia, EstadoCivil, Vinculo, StatusOptions, LinhaPesquisa
from django.forms import ModelForm

class UnidadeFederativaForm(ModelForm):
    class Meta:
        model = UnidadeFederativa
        fields = '__all__'

class SexoForm(ModelForm):
    class Meta:
        model = Sexo
        fields = '__all__'

class EtniaForm(ModelForm):
    class Meta:
        model = Etnia
        fields = '__all__'

class EstadoCivilForm(ModelForm):
    class Meta:
        model = EstadoCivil
        fields = '__all__'

class VinculoForm(ModelForm):
    class Meta:
        model = Vinculo
        fields = '__all__'

class StatusOptionsForm(ModelForm):
    class Meta:
        model = StatusOptions
        fields = '__all__'

class LinhaPesquisaForm(ModelForm):
    class Meta:
        model = LinhaPesquisa
        fields = '__all__'