# Create your views here.
from schedule.models import *
from django.http import HttpResponse
from django.utils import simplejson as json
from datetime import datetime, timedelta
def now_and_next(request):
    """ This will provide a json dictionary with the "Now and next talks"
    We define 'now' as "already began, not finished yet" and 'next'
    as "will start in the next hour"
    """
    time = datetime.now()
    now = Session.objects.filter(time_slot__begin__lt= time,
                                 time_slot__end__gt= time )
    tr = (
        datetime.now(),
        datetime.now()
        )
    nexts = Session.objects.filter(
        time_slot__begin__range=(time, time + timedelta(hours=2000))
        )

    data = {}
    data['time'] = time.isoformat()
    data['now'] = []
    for s in now:
        d = {}
        d['title'] = s.title
        d['room'] = s.room
        data['now'].append(d)

    data['next'] = []

    for s in nexts:
        d = {}
        d['title'] = unicode(s.title)
        d['room'] = unicode(s.room)
        d['begin'] = s.time_slot.begin.isoformat()
        data['next'].append(d)

    encoded = json.dumps(data)
    response = HttpResponse(encoded, mimetype = "application/json")
    return response
