from django import forms
from .models import Matricula, Probatorio

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ['numero', 'probatorio', 'requisita_bolsa']


class ProbatorioForm(forms.ModelForm):

    class Meta:
        model = Probatorio
        fields = ['data_inscricao', 'nota', 'aluno']