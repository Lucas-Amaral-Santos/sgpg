from django import forms
from .models import Disciplina, DisciplinaOfertada

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = '__all__'

class DisciplinaOfertadaForm(forms.ModelForm):
    
    class Meta:
        model = DisciplinaOfertada
        fields = '__all__'