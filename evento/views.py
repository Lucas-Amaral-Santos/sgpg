from django.shortcuts import render, redirect
from calendar import HTMLCalendar
from datetime import datetime
from .models import Evento, Participante, Convidados
from .forms import EventoForm, ParticipanteForm, ConvidadosForm
from dateutil.relativedelta import relativedelta
from django.contrib import messages

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
            eventos_dia = '<i class="fa-solid fa-circle fa-lg"></i><span class="n-event" style="margin-left: -14px;font-size:10pt;"><b>%d</b></span>' % (n_events)

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
    data_aux = datetime(year=ano, month=mes, day=datetime(ano, mes, 1).day)
    calendario = EventCalendar().formatmonth(ano, mes)
    n_month =  data_aux + relativedelta(months=1)
    p_month =  data_aux + relativedelta(months=-1)
    eventos = Evento.objects.all()
    return render(request, 'calendario.html', {'mes': mes, 'ano': ano, 'calendario': calendario, 'data':data, 'n_month': n_month, 'p_month': p_month, 'eventos': eventos, 'pagina': 'Calendário de Eventos'})

def cadastra_evento(request, data=datetime.today().date().strftime('%d/%m/%Y'), hora= datetime.now().time):
    data = datetime.strptime(data.replace('-','/'), '%d/%m/%Y').date()
    form_evento = EventoForm(initial={'evento_data': data, 'evento_hora':hora})
    
    if request.method == 'POST':
        form_evento = EventoForm(request.POST)
        
        if form_evento.is_valid():
            # Create object
            novo_evento = Evento.objects.create(
                evento = form_evento.cleaned_data['evento'],
                evento_data = form_evento.cleaned_data['evento_data'],
                evento_hora = form_evento.cleaned_data['evento_hora'],
                evento_tipo = form_evento.cleaned_data['evento_tipo'],
                evento_trabalho_final = form_evento.cleaned_data['evento_trabalho_final'],
                cadastrado_por = request.user,
            )

            novo_evento.save()
            messages.success(request, 'Evento cadastrado com sucesso!')
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
            messages.success(request, 'Participante cadastrado com sucesso!')
        return redirect('evento:detalhes_evento', evento=evento.slug)
    
    return render(request, 'cadastra_participante.html', {'form_participante': form_participante, 'evento':evento, 'pagina': 'Cadastra Participante'})


def cadastra_convidado(request, evento):
    evento = Evento.objects.get(slug=evento)
    form_convidado = ConvidadosForm()
    
    if request.method == 'POST':
        form_convidado = ConvidadosForm(request.POST)
        if form_convidado.is_valid():
            novo_convidado = Convidados.objects.create(
                convidado = form_convidado.cleaned_data['convidado'],
                convidado_tipo = form_convidado.cleaned_data['convidado_tipo'],
                evento = evento,
            )
            novo_convidado.save()
            messages.success(request, 'Convidado cadastrado com sucesso!')
        return redirect('evento:detalhes_evento', evento=evento.slug)
    
    return render(request, 'cadastra_participante.html', {'form_participante': form_convidado, 'evento':evento, 'pagina': 'Cadastra Participante'})


def detalhes_evento(request, evento):
    evento = Evento.objects.get(slug=evento)
    participantes_cadastradas = Participante.objects.filter(evento=evento.slug)
    convidados_cadastrados = Convidados.objects.filter(evento=evento.slug)

    return render(request, 'detalhes_evento.html', {'evento': evento, 'participantes_cadastradas':participantes_cadastradas, 'convidados_cadastrados': convidados_cadastrados})

