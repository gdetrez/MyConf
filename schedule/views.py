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

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from myconf.schedule.models import *

def schedule(request):
    friday = []
    for ts in TimeSlot.objects.filter(begin__day=11):
        friday.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id)))

    sat_am = []
    ts = TimeSlot.objects.filter(begin__day=12)
    filtered_ts = [t for t in ts if t.begin.hour < 13]
    for ts in filtered_ts:
        sat_am.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id)))

    sat_pm = []
    ts = TimeSlot.objects.filter(begin__day=12)
    filtered_ts = [t for t in ts if t.begin.hour > 13]
    for ts in filtered_ts:
        sat_pm.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id)))

    sun_am = []
    ts = TimeSlot.objects.filter(begin__day=13)
    filtered_ts = [t for t in ts if t.begin.hour < 13]
    for ts in filtered_ts:
        sun_am.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id)))

    sun_pm = []
    ts = TimeSlot.objects.filter(begin__day=13)
    filtered_ts = [t for t in ts if t.begin.hour > 13]
    for ts in filtered_ts:
        sun_pm.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id)))

    t = loader.get_template('schedule/schedule.djhtml')
    c = Context({
        'friday_sessions': friday,
        'sat_am': sat_am,
        'sat_pm': sat_pm,
    })
    return HttpResponse(t.render(c))

# def user(request, uname):
#     staff_member = User.objects.get(username=uname, groups=Group.objects.get(name="Staff"))
#     t = loader.get_template('people/staffmember.html')
#     c = Context({
#         'staff_member': staff_member,
#     })
#     return HttpResponse(t.render(c))
