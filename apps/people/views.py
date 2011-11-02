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

from django.http import HttpResponse
from django.template import RequestContext, loader
from people.models import Person
from django.shortcuts import render_to_response, get_object_or_404

def staff(request):
    staff = Person.objects.filter(staff=True).order_by("name")
    t = loader.get_template('people/staff.djhtml')
    c = RequestContext(request, {
        'staff_list': staff,
    })
    return HttpResponse(t.render(c))

def user(request, slug):
    staff_member = get_object_or_404(Person, slug=slug)
    t = loader.get_template('people/staffmember.djhtml')
    c = RequestContext(request, {
        'staff_member': staff_member,
    })
    return HttpResponse(t.render(c))

