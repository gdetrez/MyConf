from schedule.models import Session
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from django.template import defaultfilters
import os, tempfile, codecs, tarfile
from django.template import loader, Context

class Command(BaseCommand):
    args = ''
    help = 'Export talks from the database and prepare video directories'

    def handle(self, *args, **options):
        tdir = tempfile.mkdtemp()
        sessions = Session.objects.all()
        data = []
        for s in sessions:
            if s.kind in ('T','K') and s.time_slot is not None:
                # Create directory
                slug = "%s_%s" % (
                    s.time_slot.begin.strftime("%Y%m%d"),
                    defaultfilters.slugify(s.title))
                sdir = os.path.join(tdir, slug)
                os.mkdir(sdir)
                # Create info file
                info = [
                    ('title', s.title),
                    ('speakers', s.get_speakers_display()),
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
                # Create title
                t = loader.get_template('video-title.svg')
                file_path = os.path.join(sdir, "title.svg")
                f = codecs.open(file_path, 'w', encoding="utf-8")
                f.write(t.render(Context({
                            'title': s.title,
                            'by': u"by " + s.get_speakers_display(),})))
                f.close()
            tar = tarfile.open("videos.tar", "w")
            tar.add(tdir, arcname=".")
            tar.close()
