from django.db import models
from uuid import uuid1
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.template import loader, Context
from django.core.mail import send_mail

def default_editable_until():
    return datetime.now() + timedelta(0,3600)

class Submission(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField(help_text="A short abstract about your talk. You will be able to write a different absctact for the published program if you wish to.")
    speakers = models.TextField(help_text="Speakers for this talk. One name per line please.")

    contact_name = models.CharField(max_length=30, help_text="Full name")
    contact_email = models.EmailField()

    video = models.BooleanField(default=True)
    accessible = models.BooleanField(default=False)

    edit_token = models.CharField(max_length=36, default=uuid1, unique=True)
    editable_until = models.DateTimeField(default = default_editable_until)

    submission_date = models.DateTimeField(editable = False, auto_now_add = True)

    STATUSES = (
        ('A', 'Accepted'),
        ('R', 'Rejected'),
        ('S', 'Submitted'),
        )
    status = models.CharField(max_length=1, choices=STATUSES, blank=False,
                              default='S', editable = False)

    def can_edit(self):
        return self.editable_until >= datetime.now()
        
    def get_edit_url(self):
        return "%s?token=%s" % ( reverse('cfp:edit'),
                                       self.edit_token)
    
    def accept(self):
        c = Context({'submission': self})
        mail = loader.get_template('cfp/accept_mail')
        send_mail('[FSCONS 2012] Your submission have been accepted',
                  mail.render(c),
                  'program@fscons.org',
                  [self.contact_email],
                  fail_silently = True)
        self.status = 'A'
        self.save()

    def reject(self):
        c = Context({'submission': self})
        mail = loader.get_template('cfp/reject_mail')
        send_mail('[FSCONS 2012] Your submission have been rejected',
                  mail.render(c),
                  'program@fscons.org',
                  [self.contact_email],
                  fail_silently = True)
        self.status = 'R'
        self.save()

