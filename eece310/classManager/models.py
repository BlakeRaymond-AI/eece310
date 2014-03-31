from django.contrib.auth.models import User
from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    calendar = models.ForeignKey(Calendar)
    name = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    tags = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User)
    datetime = models.DateTimeField()
    message = models.CharField(max_length=10000)
    event = models.ForeignKey(Event)
