from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Evento
from .forms import EventoForm
from dateutil.relativedelta import relativedelta


class EventCalendar(HTMLCalendar):

    def formatday(self, day, month, weekday,):
        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        if day == datetime.today().day and month == datetime.today().month:
            return '<td class="dia-hoje" data-toggle="modal" data-target="#eventos-dia">%d</td>' % (day)
        else:
            return '<td class="dias" data-toggle="modal" data-target="#eventos-dia">%d</td>' % (day)

def mostra_eventos(request, mes, ano):
    data = datetime.today
    data_aux = datetime(ano, mes, datetime.today().day)
    calendario = EventCalendar().formatmonth(ano, mes)
    n_month =  data_aux + relativedelta(months=1)
    p_month =  data_aux + relativedelta(months=-1)
    return render(request, 'calendario.html', {'mes': mes, 'ano': ano, 'calendario': calendario, 'data':data, 'n_month': n_month, 'p_month': p_month})

def cadastra_evento(request):
    form_evento = EventoForm()

    if request.method == 'POST':
        form_evento = EventoForm(request.POST)
        if form_evento.is_valid():
            pass

    return render(request, 'cadastra_evento.html', {'form_evento': form_evento, 'pagina': 'Adicionar Novo Evento'})