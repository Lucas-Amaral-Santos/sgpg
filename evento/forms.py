from django.forms import ModelForm, DateField, TextInput
from .models import Evento, Participante, Convidados

class EventoForm(ModelForm):
    evento_data = DateField(widget=TextInput(attrs={'type':'date'}), label="Data do evento:")
    class Meta:
        model = Evento
        fields = ['evento', 'evento_data', 'evento_hora', 'evento_trabalho_final', 'evento_tipo', 'evento_obs']
        exclude = ['slug', 'updated', 'dt_cadastro', 'cadastrado_por']


class ParticipanteForm(ModelForm):
    
    class Meta:
        model = Participante
        fields = ['participante_professor', 'participante_tipo']

class ConvidadosForm(ModelForm):
    
    class Meta:
        model = Convidados
        fields = ['convidado', 'convidado_tipo']
