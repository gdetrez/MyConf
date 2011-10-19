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

from myconf.apps.schedule.models import *
from django.contrib import admin
from myconf.apps.people.models import Person

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'begin_time', 'end_time', 'duration')

admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Room)

def session_count(track):
    return track.sessions.count()

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'color', session_count)
    list_display_links = ('name',)
    prepopulated_fields = {
        'slug': ['name']
        }

admin.site.register(Track, TrackAdmin)


class PresenterInline(admin.TabularInline):
    verbose_name = "Presenter"
    verbose_name_plural = "Presenters"
    model = Session.presenters.through
    extra = 1

def presenter_list(obj):
    return u", ".join(map(unicode, obj.presenters.all()))
presenter_list.short_description = 'Presenters'
presenter_list.allow_tags = True

class SessionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
                'fields': ('title', 'kind',
                           'description', 'intended_audience', 'tags')
        }),
        ('Scheduling', {
                'classes':('collapse',),
                'fields': ('track', 'time_slot', 'room')
        }),
    )
    inlines = [
        PresenterInline,
    ]
    list_display = (unicode, presenter_list,
                    'time_slot', 'room')
    list_display_links = (unicode,)
    list_editable = ('time_slot', 'room')
    list_filter = ('kind', 'room')
    search_fields = ('title', 'description', 'intended_audience',
                     'presenters__name')

admin.site.register(Session, SessionAdmin)
