from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm
from dateutil.relativedelta import relativedelta

class EventCalendar(HTMLCalendar):

    

    def formatday(self, day, month, year, weekday,):
        eventos_dia = ''
        data = None
        if day != 0:
            data = datetime(year, month, day)
        if self.get_events(data):
            eventos_dia = '<i class="fa-solid fa-circle"></i>'


        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        if day == datetime.today().day and month == datetime.today().month and year == datetime.today().year:
                return '<td class="dia-hoje" data-toggle="modal" data-target="#eventos-dia">%d<br>%s</td>' % (day, eventos_dia)
        else:
            return '<td class="dias" data-toggle="modal" data-target="#eventos-dia">%d<br>%s</td>' % (day, eventos_dia)

    def get_events(self, data):
        if Evento.objects.filter(evento_data=data):
            return True
        else:
            return False


def mostra_eventos(request, mes=datetime.today().month, ano=datetime.today().year):
    data = datetime.today
    data_aux = datetime(ano, mes, datetime.today().day)
    calendario = EventCalendar().formatmonth(ano, mes)
    n_month =  data_aux + relativedelta(months=1)
    p_month =  data_aux + relativedelta(months=-1)
    eventos = Evento.objects.all()
    return render(request, 'calendario.html', {'mes': mes, 'ano': ano, 'calendario': calendario, 'data':data, 'n_month': n_month, 'p_month': p_month, 'eventos': eventos})

def cadastra_evento(request):
    form_evento = EventoForm()
    
    if request.method == 'POST':
        form_evento = EventoForm(request.POST)
        
        if form_evento.is_valid():
            # Create object
            novo_evento = Evento.objects.create(
                evento = form_evento.cleaned_data['evento'],
                evento_data = form_evento.cleaned_data['evento_data'],
                evento_hora = form_evento.cleaned_data['evento_hora'],
                evento_trabalho_final = form_evento.cleaned_data['evento_trabalho_final'],
                cadastrado_por = request.user,
            )

            novo_evento.save()
            return redirect('evento:detalhes_evento', evento=novo_evento.slug)

    return render(request, 'cadastra_evento.html', {'form_evento': form_evento, 'pagina': 'Adicionar Novo Evento'})

def cadastra_participante(request, evento):
    evento = Evento.objects.get(slug=evento)
    form_participante = ParticipanteForm()
    
    if request.method == 'POST':
        form_participante = ParticipanteForm(request.POST)
        if form_participante.is_valid():
            novo_participante = Participante.objects.create(
                participante_professor = form_participante.cleaned_data['participante_professor'],
                participante_tipo = form_participante.cleaned_data['participante_tipo'],
                evento = evento,
            )
            novo_participante.save()
        return redirect('evento:detalhes_evento', evento=evento.slug)
    
    return render(request, 'cadastra_participante.html', {'form_participante': form_participante})

def detalhes_evento(request, evento):
    evento = Evento.objects.get(slug=evento)
    participantes_cadastradas = Participante.objects.filter(evento=evento.slug)

    return render(request, 'detalhes_evento.html', {'evento': evento, 'participantes_cadastradas':participantes_cadastradas})

