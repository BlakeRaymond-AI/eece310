from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from models import Calendar, Event
from forms import CalendarForm, EventForm

def index(request):
    return HttpResponse("You're at the main page for Class Manager.")

@login_required
def view_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, pk=calendar_id)
    events = Event.objects.filter(calendar=calendar)
    return render(request, "calendar.html", {"calendar": calendar, "events": events})

@login_required
def view_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    calendar = event.calendar
    return render(request, "event.html", {"calendar": calendar, "event": event})

@login_required
def create_calendar(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save()
            return HttpResponseRedirect(reverse("view_calendar", args=[calendar.id]))
    else:
        form = CalendarForm()

    return render(request, 'create_calendar.html', {'form': form})

@login_required
def create_event(request, calendar_id):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            calendar = get_object_or_404(Calendar, pk=calendar_id)
            datetime = form.cleaned_data['datetime']
            name = form.cleaned_data['name']
            tags = form.cleaned_data['tags']
            event = Event.objects.create(calendar=calendar, datetime=datetime, name=name, tags=tags)
            event.save()
            return HttpResponseRedirect(reverse("view_calendar", args=[calendar.id]))
        else:
            return HttpResponse(form.errors)
    form = EventForm()
    return render(request, 'create_event.html', {'form': form, 'calendar_id': calendar_id})

