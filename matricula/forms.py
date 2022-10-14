from dataclasses import field
from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ['numero', 'probatorio']