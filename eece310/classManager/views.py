from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from models import Calendar, Event, Message
from forms import CalendarForm, EventForm, MessageForm, TagSearchForm

from datetime import datetime

def index(request):
    return HttpResponse("You're at the main page for Class Manager.")

@login_required
def view_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, pk=calendar_id)
    events = Event.objects.filter(calendar=calendar)
    form = TagSearchForm()
    return render(request, "calendar.html", {"calendar": calendar, "events": events, "tag_search_form": form})

@login_required
def view_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    calendar = event.calendar
    form = MessageForm()
    messages = Message.objects.filter(event=event).order_by('datetime')
    return render(request, "event.html", {"calendar": calendar, "event": event, "messages": messages, "form": form})

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

@login_required
def post_message(request, event_id):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            event = get_object_or_404(Event, pk=event_id)
            message = form.cleaned_data['message']
            user = request.user
            message_obj = Message.objects.create(event=event, datetime=datetime.now(), user=user, message=message)
            return HttpResponseRedirect(reverse("view_event", args=[event_id]))
        else:
            return HttpResponse(form.errors)

@login_required
def tag_search(request, calendar_id):
    if request.method == "POST":
        form = TagSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            calendar = get_object_or_404(Calendar, pk=calendar_id)
            matches = Event.objects.filter(tags__icontains=query, calendar=calendar)
            return render(request, "tag_search.html", {"calendar": calendar, "events": matches, "query": query})
