from .models import Colegiado
from django.forms import DateField, TextInput, ModelForm
from datetime import datetime

class ColegiadoForm(ModelForm):
    colegiado_data_entrada = DateField(label='Data de entrada:', required=False, widget=TextInput(attrs={'type':'date'}))
    colegiado_data_saida = DateField(label='Data de término:', required=False, widget=TextInput(attrs={'type':'date'}), initial=datetime.today().strftime('%d/%m/%Y'))
    class Meta:
        model = Colegiado
        fields = '__all__'
        exclude = ['professor_membro', 'matricula_membro']