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
from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from myconf.schedule.models import *

#@login_required(login_url='/admin/')
def schedule(request):
    friday = []
    for ts in TimeSlot.objects.filter(begin__day=11):
        friday.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id), ts.passed()))

    sat_am = []
    ts = TimeSlot.objects.filter(begin__range=(
            datetime(2011, 11, 12, 9, 15),
            datetime(2011, 11, 12, 12, 00)
            ))
    for ts in ts:
        sat_am.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id), ts.passed()))

    sat_pm = []
    ts = TimeSlot.objects.filter(begin__range=(
            datetime(2011,11,12,14,15),
            datetime(2011,11,12,18,15)
            ))
    for ts in ts:
        sat_pm.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id), ts.passed()))

    sun_am = []
    ts = TimeSlot.objects.filter(begin__range=(
            datetime(2011,11,13, 9,15),
            datetime(2011,11,13,12,00)
            ))
    for ts in ts:
        sun_am.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id), ts.passed()))

    sun_pm = []
    ts = TimeSlot.objects.filter(begin__range=(
            datetime(2011,11,13,14,15),
            datetime(2011,11,13,18,15)
            ))
    for ts in ts:
        sun_pm.append(("%s" % (str(ts.begin.time())[0:5]), Session.objects.filter(time_slot__id = ts.id), ts.passed()))

    t = loader.get_template('schedule/schedule.djhtml')
    c = RequestContext(request,{
        'friday_sessions': friday,
        'sat_am': sat_am,
        'sat_pm': sat_pm,
        'sun_pm': sun_pm,
        'sun_am': sun_am,
    })
    return HttpResponse(t.render(c))

def track(request, slug):
    track = get_object_or_404(Track, slug=slug)
    t = loader.get_template('schedule/track.djhtml')
    c = RequestContext(request,{
            'track': track,
            })
    return HttpResponse(t.render(c))

def session(request, pk):
    session = get_object_or_404(Session, pk=pk, time_slot__isnull=False)

    # shortcut variable to this session begin and end times
    begin = session.time_slot.begin
    end = session.time_slot.end
    # Session starting up to 30 minutes after the end
    # of this one
    timerange = (end, end + timedelta(minutes=30))
    sessions_after = Session.objects.filter(
        time_slot__begin__range=timerange).order_by('time_slot__begin')
        
    # Concurrent sessions
    query = Q(time_slot__begin__lt = end) & Q(time_slot__end__gt = begin)
    concurrent_sessions = Session.objects.filter(query).exclude(pk=pk).order_by('time_slot__begin')
        
        
    # 3 next talks in the same room
    next_sessions_in_room = Session.objects.filter(
        room=session.room,
        time_slot__begin__gte = end,
        time_slot__begin__year = begin.year,
        time_slot__begin__month = begin.month,
        time_slot__begin__day = begin.day
        ).exclude(pk=pk).order_by('time_slot__begin')[:3]
    
    t = loader.get_template('schedule/session_detail.djhtml')
    c = RequestContext(request,{
            'session': session,
            'sessions_after': sessions_after,
            'concurrent_sessions': concurrent_sessions,
            'next_sessions_in_room': next_sessions_in_room,
            })
    return HttpResponse(t.render(c))
