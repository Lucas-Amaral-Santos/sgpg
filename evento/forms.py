from django.forms import ModelForm, DateField, TextInput
from .models import Evento, Participante

class EventoForm(ModelForm):
    evento_data = DateField(widget=TextInput(attrs={'type':'date'}))
    class Meta:
        model = Evento
        fields = '__all__'
        exclude = ['slug', 'updated', 'dt_cadastro', 'cadastrado_por']

class ParticipanteForm(ModelForm):
    
    class Meta:
        model = Participante
        fields = ['participante_professor', 'participante_tipo']
