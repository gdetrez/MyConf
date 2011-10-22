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
from myconf.apps.schedule.models import *
from taggit.models import Tag

#@login_required(login_url='/admin/')
def schedule(request):
    tracks = Track.objects.all().order_by("name")
    sessions = Session.objects.filter(time_slot__isnull = False).order_by("time_slot__begin", "room")

    t = loader.get_template('schedule/schedule.djhtml')
    c = RequestContext(request,{
        'sessions': sessions,
        'tracks': tracks,
    })
    return HttpResponse(t.render(c))

def track(request, slug):
    track = get_object_or_404(Track, slug=slug)
    t = loader.get_template('schedule/track.djhtml')
    c = RequestContext(request,{
            'track': track,
            'sessions': track.sessions.all().order_by("time_slot__begin"),
            })
    return HttpResponse(t.render(c))

def tag(request, slug):
    """ Return a list of session and presenters associated with a certain
    tag.
    """
    tag = get_object_or_404(Tag, slug=slug)
    sessions = Session.objects.filter(tags__slug__in=[slug], time_slot__isnull=False)
    speakers = Person.objects.filter(talks__in = sessions, talks__time_slot__isnull=False)
    t = loader.get_template('schedule/tag.djhtml')
    c = RequestContext(request,{
            'tag': tag,
            'sessions': sessions,
            'speakers': speakers,
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
            'signedup':request.GET.get('signedup',None) == 'ok'
            })
    return HttpResponse(t.render(c))