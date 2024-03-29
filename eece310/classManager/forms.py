from django import forms

from models import Calendar

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar

class EventForm(forms.Form):
    name = forms.CharField(max_length=255)
    datetime = forms.DateTimeField()
    tags = forms.CharField(max_length=255)

class MessageForm(forms.Form):
    message = forms.CharField(max_length=10000)

class TagSearchForm(forms.Form):
    query = forms.CharField(max_length=255)
