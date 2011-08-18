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

from myconf.schedule.models import *
from django.contrib import admin

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'begin_time', 'end_time', 'duration')

admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Room)

def color(obj):
    return """
<div style=\"height:1em;background:%s;border:thin solid black;\"></div>
""" % obj.get_html_color()
color.short_description = 'Color'
color.allow_tags = True
color.admin_order_field = 'color'

class TrackAdmin(admin.ModelAdmin):
    list_display = (color, 'name')
    list_display_links = ('name',)

admin.site.register(Track, TrackAdmin)

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3

class PresenterInline(admin.TabularInline):
    model = Presenter
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
                'fields': ('title', 'kind',
                           'description', 'intended_audience', )
        }),
        ('Scheduling', {
                'classes':('collapse',),
                'fields': ('track', 'time_slot', 'room')
        }),
    )
    inlines = [
        PresenterInline,
    ]
    list_display = ('title', 'time_slot', 'room')


admin.site.register(Session, SessionAdmin)
admin.site.register(Presenter)
