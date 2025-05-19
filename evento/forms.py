from django.forms import ModelForm, DateField, TextInput, ChoiceField
from .models import Evento, Participante, Convidados
from matricula.models import TrabalhoFinal
from django.db.models import Q

class EventoForm(ModelForm):
    evento_data = DateField(widget=TextInput(attrs={'type':'date'}), label="Data do evento:")


    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['evento_trabalho_final'].queryset = TrabalhoFinal.objects.filter(Q(matricula__probatorio__aluno__status__status__status_options='Ativo')|Q(matricula__probatorio__aluno__status__status__status_options='Probatório')) 

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
