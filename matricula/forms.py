from django import forms
from .models import Afastamento, Bolsa, Matricula, Probatorio, Inscricao, TrabalhoFinal, InscricaoProbatorio, VersaoFinal, Nota, Orientacao
import datetime

class ProbatorioMatriculaForm(forms.ModelForm):

    def __init__(self, matricula,  *args, **kwargs):
        super(ProbatorioMatriculaForm, self).__init__(*args, **kwargs)
        self.fields['grau'] = Matricula.objects.get(slug=matricula).probatorio.grau
        self.fields['probatorio'] = Matricula.objects.get(slug=matricula).probatorio

    class Meta:
        model = Matricula
        fields = ['numero', 'probatorio', 'grau', 'requisita_bolsa', 'dt_matricula']


class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ['numero', 'probatorio', 'grau', 'requisita_bolsa', 'dt_matricula']

class ProbatorioForm(forms.ModelForm):
    data_inscricao = forms.DateField(label="Data de Inscrição:", widget=forms.NumberInput(attrs={'type':'date'}))

    class Meta:
        model = Probatorio
        fields = ['data_inscricao', 'aluno', 'grau']

class AlunoProbatorioForm(forms.ModelForm):
    data_inscricao = forms.DateField(label="Data de Inscrição:", widget=forms.NumberInput(attrs={'type':'date'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Probatorio
        fields = ['data_inscricao', 'grau']

class BolsaForm(forms.ModelForm):

    class Meta:
        model = Bolsa
        fields = ['iniciacao_cientifica', 'nome', 'agencia', 'dt_inicio']

class AfastamentoForm(forms.ModelForm):

    class Meta:
        model = Afastamento
        fields = ['motivo', 'saida', 'retorno']

class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = ['disciplina_ofertada', 'nota']

class InscricaoProbatorioForm(forms.ModelForm):

    class Meta:
        model = InscricaoProbatorio
        fields = ['disciplina_ofertada', 'nota']

class TrabalhoFinalForm(forms.ModelForm):

    class Meta:
        model = TrabalhoFinal
        fields = ['titulo', 'resumo']

class VersaoFinalForm(forms.ModelForm):
    class Meta:
        model = VersaoFinal
        fields =['versao_final']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields =['nota']

class LinhaPesquisaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ['linha_pesquisa']

class OrientacaoForm(forms.ModelForm):
    
    class Meta:
        model = Orientacao
        fields = ['professor', 'tipo', 'professor_externo']