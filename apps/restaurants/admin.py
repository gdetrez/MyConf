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

from restaurants.models import *
from django.contrib import admin

def opening_times_list(r):
    return u"; ".join(map(unicode, r.opening_times.all()))
opening_times_list.short_description = 'Opening times'

class OpeningTimeInline(admin.TabularInline):
#    verbose_name = "Presenter"
#    verbose_name_plural = "Presenters"
    model = OpeningTime
    extra = 1

# def presenter_list(obj):
#     return u", ".join(map(unicode, obj.presenters.all()))
# presenter_list.short_description = 'Presenters'
# presenter_list.allow_tags = True

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
                'fields': ('name', 'one_line_description',
                           'description', 'website',)
                }),
        ('Location', {
    #            'classes':('collapse',),
                'fields': ('distance', 'lattitude', 'longitude')
                }),
        )
    inlines = [
        OpeningTimeInline,
    ]

    list_display = ('name', 'one_line_description', 'distance_unit', 
                    opening_times_list, 'open')
    list_display_links = ('name',)
    search_fields = ('name', 'one_line_description', 'description')

admin.site.register(Restaurant, RestaurantAdmin)
