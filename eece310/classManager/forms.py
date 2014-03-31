from django import forms

from models import Calendar

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
