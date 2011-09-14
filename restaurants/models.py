# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class OpeningTime(models.Model):
    restaurant = models.ForeignKey('Restaurant',related_name='opening_times')
    begin = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        unique_together = (('restaurant', 'begin', 'end'),)

    
    def is_now(self):
        return self.begin <= datetime.now() and self.end > datetime.now()
        # def __unicode__(self):
    #     return u"%s – %s" % (self.begin.strftime('%A %d, %H.%M'),
    #                          self.end.strftime('%H.%M'))

class Restaurant(models.Model):
    name = models.CharField(max_length=80)
    one_line_description = models.CharField(max_length=200)
    distance = models.IntegerField()
    description = models.TextField(blank=True, help_text="Uses <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown</a> syntax")
    website = models.URLField(blank=True)

    lattitude = models.FloatField()
    longitude = models.FloatField()

    def open(self):
        for ot in self.opening_times.all():
            if ot.is_now():
                return True
        return False
    
    def distance_unit(self):
        return u"%dm" % self.distance
