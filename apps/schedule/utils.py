from .models import Session
from django.db.models import Q
from datetime import timedelta

def get_concurrent_sessions(session):
    # shortcut variable to this session begin and end times
    begin = session.time_slot.begin
    end = session.time_slot.end
    query = Q(time_slot__begin__lt = end) & Q(time_slot__end__gt = begin)
    return Session.objects.filter(query).exclude(pk=session.pk).order_by('time_slot__begin')

def get_following_sessions(session, minutes):

    # shortcut variable to this session begin and end times
    begin = session.time_slot.begin
    end = session.time_slot.end
    # Session starting up to x minutes after the end
    # of this one
    timerange = (end, end + timedelta(minutes=minutes))
    return Session.objects.filter(time_slot__begin__range=timerange).order_by('time_slot__begin')

def get_next_n_sessions_in_room(session, n):
    # shortcut variable to this session begin and end times
    begin = session.time_slot.begin
    end = session.time_slot.end
    # 3 next talks in the same room
    return Session.objects.filter(
        room=session.room,
        time_slot__begin__gte = end,
        time_slot__begin__year = begin.year,
        time_slot__begin__month = begin.month,
        time_slot__begin__day = begin.day
        ).exclude(pk=session.pk).order_by('time_slot__begin')[:n]
