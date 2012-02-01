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

    def mkFileName(self, session):
        """Build a safe file name from the session information"""
        title = defaultfilters.slugify(session.title)
        return "%s" % (title)


    def handle(self, *args, **options):
        tdir = tempfile.mkdtemp()
        sessions = Session.objects.all()
        data = []
        tar = tarfile.open("videos.tar", "w")
        for s in sessions:
            if s.kind in ('T','K') and s.time_slot is not None:
                # Create directory
                slug = self.mkFileName(s)
                sdir = os.path.join(tdir, slug)
                os.mkdir(sdir)
                # Create metadata file
                t = loader.get_template('video-metadata.xml')
                file_path = os.path.join(sdir, "metadata.xml")
                f = codecs.open(file_path, 'w', encoding="utf-8")
                f.write(t.render(Context({'session':s})))
                f.close()
                # Create title
                t = loader.get_template('video-title.svg')
                file_path = os.path.join(sdir, "title.svg")
                f = codecs.open(file_path, 'w', encoding="utf-8")
                f.write(t.render(Context({
                            'title': s.title,
                            'by': u"by " + s.get_speakers_display(),})))
                f.close()
                tar.add(sdir, arcname=slug)
        tar.close()
