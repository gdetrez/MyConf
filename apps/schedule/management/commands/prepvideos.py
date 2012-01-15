from schedule.models import Session
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from django.template import defaultfilters
import os, tempfile, codecs, tarfile

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("Neither json or simplejson are available on your system")


def speakers(session):
    r = ""
    presenters = session.presenters.all()
    for i, person in enumerate(presenters):
        if i!=0 and i != len(presenters) -1:
            r += ", "
        elif i!=0 and i==len(presenters) -1:
            r += " & "
        r+= unicode(person)
    return r

class Command(BaseCommand):
    args = ''
    help = 'Export talks from the database and prepare video directories'

    def handle(self, *args, **options):
        tdir = tempfile.mkdtemp()
        sessions = Session.objects.all()
        data = []
        for s in sessions:
            if s.kind in ('T','K') and s.time_slot is not None:
                slug = "%s_%s" % (
                    s.time_slot.begin.strftime("%Y%m%d"),
                    defaultfilters.slugify(s.title))
                sdir = os.path.join(tdir, slug)
                os.mkdir(sdir)
                info = [
                    ('title', s.title),
                    ('speakers', speakers(s)),
                    ('date', s.time_slot.begin.strftime("%Y-%m-%d")),
                    ('time', s.time_slot.begin.strftime("%H:%M")),
                    ('room', s.room.name),
                    ('kind', s.get_kind_display()),
                    ('description', s.description),
                    ]
                file_path = os.path.join(sdir, "info.txt")
                f = codecs.open(file_path, 'w', encoding="utf-8")
                for a,b in info:
                    f.write("%s: %s\n" % (a,b))
                f.close()
            tar = tarfile.open("videos.tar", "w")
            tar.add(tdir, arcname=".")
            tar.close()
