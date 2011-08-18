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


class Profile(models.Model):
    user = models.OneToOneField(User)

    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="avatars", blank=True)
    #team involvement??
    blog = models.URLField(blank=True, verify_exists=False)
    microblog = models.URLField(blank=True, verify_exists=False)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    micro_biography = models.CharField(max_length=140, blank=True)
    physical_location = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
