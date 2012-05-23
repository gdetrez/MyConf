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

from .models import *
from django.contrib import admin

def action_accept(modeladmin, request, queryset):
    for s in queryset:
        s.accept()
action_accept.short_description = "Mark selected submission as accepted. Notify speaker"

def action_reject(modeladmin, request, queryset):
    for s in queryset:
        s.reject()
action_reject.short_description = "Mark selected submission as rejected. Notify speaker"

class SubmissionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
                'fields': ('title', 'abstract','speakers')}),
        ('Contact information', {
                'fields': ('contact_name', 'contact_email')}),
        ('Meta', {
                'fields': ('video', 'accessible')}),
        ('Edit info', {
                'classes':('collapse',),
                'fields': ('edit_token', 'editable_until')}),
    )
    list_display = ('title', 'status', 'contact_name', 'video', 'accessible')
    #                 'time_slot', 'room')
    # list_display_links = (unicode,)
    # list_editable = ('time_slot', 'room')
    list_filter = ('status','video', 'accessible')
    search_fields = ('title', 'abstract', 'speakers',
                     'contact_name', 'contact_email')
    actions = [action_accept, action_reject]

admin.site.register(Submission, SubmissionAdmin)
