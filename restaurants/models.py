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
from datetime import datetime

class OpeningTime(models.Model):
    restaurant = models.ForeignKey('Restaurant',related_name='opening_times')
    begin = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        unique_together = (('restaurant', 'begin', 'end'),)

    
    def is_now(self):
        return self.begin <= datetime.now() and self.end > datetime.now()

    def __unicode__(self):
        return u"%s – %s" % (self.begin.strftime('%A %d: %H.%M'),
                             self.end.strftime('%H.%M'))

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
    open.short_description = 'Open now'

    def distance_unit(self):
        return u"%dm" % self.distance
    distance_unit.short_description = 'Walking distance'
