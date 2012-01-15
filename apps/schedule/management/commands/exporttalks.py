from schedule.models import Session
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("Neither json or simplejson are available on your system")

class Command(BaseCommand):
    args = ''
    help = 'Export talks from the database'

    def handle(self, *args, **options):
        sessions = Session.objects.all()
        data = [{
                'title': s.title,
                'description': s.description,
                'room': s.room.name,
                'kind': s.get_kind_display(),
                'speakers': [p.name for p in s.presenters.all()],
                } for s in sessions if s.kind in ('T','K') and s.time_slot is not None]
        print json.dumps(data)
