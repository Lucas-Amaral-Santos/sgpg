from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm
from dateutil.relativedelta import relativedelta

class EventCalendar(HTMLCalendar):

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="%s">' % (
            self.cssclass_month))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, m=themonth, y=theyear))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def formatweek(self, theweek, m=None, y=None):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, m, y, wd) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s
    
    def formatday(self, day, month, year, weekday,):
        eventos_dia = ''
        data = None
        if day != 0:
            data = datetime(year, month, day)
        n_events=self.get_events(data)
        if n_events:
            eventos_dia = '<i class="fa-solid fa-circle"></i><span class="n-event" style="margin-left: -12px;font-size:10pt;"><b>%d</b></span>' % (n_events)


        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        if day == datetime.today().day and month == datetime.today().month and year == datetime.today().year:
                return '<td class="dia-hoje dias %s" data-toggle="modal" data-target="#eventos-dia"><span id="dia-invisivel">%d/%d/%d</span><span class="dia">%d</span><br>%s</td>' % (weekday, day, month, year, day, eventos_dia)
        else:
            return '<td class="dias %s" data-toggle="modal" data-target="#eventos-dia"><span id="dia-invisivel">%d/%d/%d</span><span class="dia">%d</span><br>%s</td>' % (weekday, day, month, year, day, eventos_dia)

    def get_events(self, data):
        evento = Evento.objects.filter(evento_data=data)
        if evento:
            return evento.count()



def mostra_eventos(request, mes=datetime.today().month, ano=datetime.today().year):
    data = datetime.today
    data_aux = datetime(ano, mes, datetime.today().day)
    calendario = EventCalendar().formatmonth(ano, mes)
    n_month =  data_aux + relativedelta(months=1)
    p_month =  data_aux + relativedelta(months=-1)
    eventos = Evento.objects.all()
    return render(request, 'calendario.html', {'mes': mes, 'ano': ano, 'calendario': calendario, 'data':data, 'n_month': n_month, 'p_month': p_month, 'eventos': eventos})

def cadastra_evento(request, data=datetime.today().date().strftime('%d/%m/%Y'), hora= datetime.now().time):

    form_evento = EventoForm(initial={'evento_data': data.replace('-','/'), 'evento_hora':hora})
    
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
    
    return render(request, 'cadastra_participante.html', {'form_participante': form_participante, 'evento':evento, 'pagina': 'Cadastra Participante'})

def detalhes_evento(request, evento):
    evento = Evento.objects.get(slug=evento)
    participantes_cadastradas = Participante.objects.filter(evento=evento.slug)

    return render(request, 'detalhes_evento.html', {'evento': evento, 'participantes_cadastradas':participantes_cadastradas})

