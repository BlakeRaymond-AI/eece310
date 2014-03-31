from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from models import Calendar
from forms import CalendarForm

def index(request):
    return HttpResponse("You're at the main page for Class Manager.")

@login_required
def view_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, pk=calendar_id)
    return HttpResponse("You're viewing calendar \"%s.\"" % calendar.name)

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
