from people.models import Person
from optparse import make_option

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
    option_list = BaseCommand.option_list + (
        make_option('--tsv',
            action='store_true',
            dest='tsv',
            default=False,
            help='Export as tab separated instead of json'),
        )

    def handle(self, *args, **options):
        speakers = Person.objects.annotate(num_talks=Count('talks')).filter(num_talks__gt=0)
        data = [{'name': s.name, 'speaker': True, 'mail':s.email} for s in speakers]
        if options['tsv']:
            for row in data:
                print "%s\t%s" % (row['name'], row['mail'])
        else: 
            print json.dumps(data)
