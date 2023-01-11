from django.forms import ModelForm
from .models import Evento, Participante

class EventoForm(ModelForm):
    
    class Meta:
        model = Evento
        fields = '__all__'
        exclude = ['slug', 'updated', 'dt_cadastro', 'cadastrado_por']

class ParticipanteForm(ModelForm):
    
    class Meta:
        model = Participante
        fields = ['participante_professor', 'participante_tipo']
