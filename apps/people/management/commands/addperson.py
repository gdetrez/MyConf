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
    args = 'NAME'
    help = 'Export speakers from the database'
    option_list = BaseCommand.option_list + (
        make_option('--staff',
                    action='store_true',
                    dest='staff',
                    default=False,
                    help='This person is staff'),
        )

    def handle(self, *args, **options):
        name = u" ".join(map(lambda s: s.decode("utf8"),args))
        print options
        person = Person(name=name, staff=options['staff'])
        person.save()
        print person.pk

