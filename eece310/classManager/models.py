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
    