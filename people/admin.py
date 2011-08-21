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

from myconf.people.models import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'staff')
    list_display_links = ('name',)
    list_filter = ('staff', 'physical_location')
    list_editable = ('staff',)
    search_fields = ('name', 'slug', 'email', 'micro_biography', 'physical_location')
    prepopulated_fields = {
        'slug': ['name']
        }

admin.site.register(Person, PersonAdmin)
