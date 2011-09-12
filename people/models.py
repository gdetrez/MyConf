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
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Person(models.Model):
    
    name = models.CharField(max_length=30, help_text="Full name")
    slug = models.SlugField(primary_key=True,
                            help_text="The slug is used to build the URL. Could be a nickname or a ASCII representation of the name (only lowerase, numbers and hyphen)")
    photo = models.ImageField(upload_to="avatars", blank=True,)

    # Profile info
    blog = models.URLField(blank=True, verify_exists=False)
    microblog = models.URLField(blank=True, verify_exists=False,
                                help_text="status.net, identi.ca or twitter")
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True,
                                 help_text="Please include the country's prefix")

    micro_biography = models.CharField(max_length=140, blank=True,
                                       help_text="micro = imited to 140 characters.")
    physical_location = models.CharField(max_length=200, blank=True,
                                         help_text="Country or city name")

    biography = models.TextField(blank=True, help_text="For speakers' bio")

    # Flags
    staff = models.BooleanField()

    class Meta:
        ordering = ('name', )


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u"/people/%s/" % self.slug
