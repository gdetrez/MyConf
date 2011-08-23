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
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.db.models import Q

@login_required(login_url='/admin/')
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
        'sun_am': sun_am,
        'sun_pm': sun_pm,
    })
    return HttpResponse(t.render(c))


def session(request, pk):
    session = Session.objects.get(pk=pk)
    # Session starting up to 30 minutes after the end
    # of this one
    timerange = (
        session.time_slot.end,
        session.time_slot.end + timedelta(minutes=30))
    sessions_after = Session.objects.filter(
        time_slot__begin__range=timerange).order_by('time_slot__begin')

    # Concurrent sessions
    timerange = (
        session.time_slot.begin,
        session.time_slot.end)
    query = Q(time_slot__begin__range=timerange) | Q(time_slot__end__range=timerange)
    concurrent_sessions = Session.objects.filter(query).exclude(pk=pk).order_by('time_slot__begin')


    # 3 next talks in the same room
    timerange = (
        session.time_slot.begin,
        session.time_slot.end)
    query = Q(time_slot__begin__range=timerange) | Q(time_slot__end__range=timerange)
    next_sessions_in_room = Session.objects.filter(
        room=session.room,
        time_slot__begin__gte=session.time_slot.end,
        time_slot__begin__year=session.time_slot.begin.year,
        time_slot__begin__month=session.time_slot.begin.month,
        time_slot__begin__day=session.time_slot.begin.day
    ).exclude(pk=pk).order_by('time_slot__begin')[:3]

    t = loader.get_template('schedule/session_detail.djhtml')
    c = Context({
            'session': session,
            'sessions_after': sessions_after,
            'concurrent_sessions': concurrent_sessions,
            'next_sessions_in_room': next_sessions_in_room,
            })
    return HttpResponse(t.render(c))
