# -*- coding: utf-8 -*-
# Copyright (C) 2011 Grégoire Détrez
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from django.db import models

# Create your models here.
from django.template.defaultfilters import date
from django.conf import settings
from django.contrib.auth.models import User
from myconf.people.models import Person

class TimeSlot(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()

    unique_together = (("begin", "end"),)

    def day(self):
        return self.begin.strftime("%A %d")

    def begin_time(self):
        return self.begin.time()

    def end_time(self):
        return self.end.time()

    def duration(self):
        return self.end - self.begin

    def __unicode__(self):
        return u"%s – %s" % (self.begin.strftime('%A %d, %H.%M'),
                             self.end.strftime('%H.%M'))

class Room(models.Model):
    name = models.CharField(max_length=200, unique = True)
    def __unicode__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=200, unique = True)
    css_class = models.CharField(max_length=16)

    def get_html_color(self):
        if self.color in ['red', 'black', 'blue', 'yellow']:
            return self.color
        else:
            return "#%s" % self.color

    def __unicode__(self):
        return self.name

# class Presenter(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(blank = True)
#     session = models.ForeignKey('Session', related_name="presenters_old")

#     def __unicode__(self):
#         return self.name

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

    presenters = models.ManyToManyField(Person, related_name='talks')
    
    unique_together = (("time_slot", "room"),)

    def __unicode__(self):
        return u"%s: %s" % (self.get_kind_display(), self.title)

    def get_absolute_url(self):
        return "/schedule/session/%i/" % self.id
