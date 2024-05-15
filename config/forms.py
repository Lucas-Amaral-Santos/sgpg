from .models import UnidadeFederativa, Sexo, Etnia, EstadoCivil, Vinculo, \
                    StatusOptions, LinhaPesquisa, Instituicao, Colegio, \
                    InstituicaoResidencia, Grau, Linguas, AgenciaFomento
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

class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'
        verbose_name = 'Instituição'

class ColegioForm(ModelForm):
    class Meta:
        model = Colegio
        fields = '__all__'

class InstituicaoResidenciaForm(ModelForm):
    class Meta:
        model = InstituicaoResidencia
        fields = '__all__'

class GrauForm(ModelForm):
    class Meta:
        model = Grau
        fields = '__all__'

class LinguasForm(ModelForm):
    class Meta:
        model = Linguas
        fields = '__all__'

class AgenciaFomentoForm(ModelForm):
    class Meta:
        model = AgenciaFomento
        fields = '__all__'