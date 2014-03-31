from django.db import models


class CalendarModel(models.Model):
    url = models.URLField()


class EventModel(models.Model):
    calendar = models.ForeignKey(CalendarModel)
    date = models.DateField()
    time = models.TimeField()


class ThreadModel(models.Model):
    event = models.OneToOneField(EventModel)


class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel)
    user = models.CharField(max_length=30)
    content = models.CharField(max_length=200)


class TagModel(models.Model):
    event = models.ForeignKey(EventModel)
    label = models.CharField(max_length=20)
