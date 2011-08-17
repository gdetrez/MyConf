from django.db import models

# Create your models here.
from django.template.defaultfilters import date
from django.conf import settings
from django.contrib.auth.models import User


class TimeSlot(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()

    unique_together = (("begin", "end"),)

    def day(self):
        return self.begin.strftime("%A %d")

    def begin_time(self):
        return self.begin.time()

    def end_time(self):
        return self.begin.time()

    def duration(self):
        return self.end - self.begin

    def __unicode__(self):
        return u"%s - %s" % (self.begin, self.end)

class Room(models.Model):
    name = models.CharField(max_length=200, unique = True)
    def __unicode__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=200, unique = True)
    color = models.CharField(max_length=6)

    def get_html_color(self):
        if self.color in ['red', 'black', 'blue', 'yellow']:
            return self.color
        else:
            return "#%s" % self.color

    def __unicode__(self):
        return self.name

class Presenter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank = True)
    session = models.ForeignKey('Session', related_name="presenters")

    def __unicode__(self):
        return self.name

SESSION_KIND_CHOICES = (
    ('T', 'Talk'),
    ('W', 'Workshop'),
    ('K', 'Keynote'),
    ('O', 'Other'),
)

class Session(models.Model):
    title = models.CharField(max_length=200, unique = True)
    description = models.TextField()
    track = models.ForeignKey('Track', blank=True, null=True)
    time_slot = models.ForeignKey('TimeSlot', blank=True, null=True)
    room = models.ForeignKey('Room', blank=True, null=True)
    intended_audience = models.TextField(blank=True)
    kind = models.CharField(max_length=1, choices=SESSION_KIND_CHOICES, default="T")

#    presenters = models.ManyToManyField(Presenter, related_name='talks')

    
    
    unique_together = (("time_slot", "room"),)

    def __unicode__(self):
        return u"%s" % (self.title)
