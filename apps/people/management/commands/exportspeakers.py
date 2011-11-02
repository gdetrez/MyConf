from people.models import Person
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("Neither json or simplejson are available on your system")
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
class Command(BaseCommand):
    args = ''
    help = 'Export speakers from the database'
    # option_list = BaseCommand.option_list + (
    #     make_option('--reset',
    #         action='store_true',
    #         dest='reset',
    #         default=False,
    #         help='Remove old timeslots before'),
    #     )

    def handle(self, *args, **options):
        speakers = Person.objects.annotate(num_talks=Count('talks')).filter(num_talks__gt=0)
        data = [{'name': s.name, 'speaker': True} for s in speakers]
        print json.dumps(data)
            
