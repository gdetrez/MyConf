from django.db import models

from django.utils import simplejson
from django.template.defaultfilters import date
from django.conf import settings

from pubsub.utils import publish

class Notification(models.Model):

    date = models.DateTimeField(auto_now_add = True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        super(Notification ,self).save(*args, **kwargs)

        payload = {}
        payload['text'] = self.text
        payload['time'] = date(self.date, settings.DATETIME_FORMAT)

        payload_json = simplejson.dumps(payload)
#        print payload_json
        publish("/test/notifications", payload_json)

