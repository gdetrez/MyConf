from notifications.models import Notification
from django.core.management.base import BaseCommand, CommandError
import time, math, random

RED = '\033[01;31m%s\033[00m'
GREEN = '\033[01;32m%s\033[00m'
BOLD = '\033[01;1m%s\033[00m'

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            while True:
                nb_notifs = self.poisson(1)
                if nb_notifs > 0:
                    print BOLD % "Generating %d notifications" % nb_notifs
                    for i in range(0, nb_notifs):
                        self.create_notification()
                time.sleep(1)
        except (KeyboardInterrupt):
            print "Bye."

    def create_notification(self, text=None):
        if text == None:
            text = self.random_string()
        n = Notification(text = text)
        n.save()

    def poisson(self, lbda):
        l = math.exp(-lbda)
        k = 1
        p = random.random()
        while p > l:
            k = k + 1.
            u = random.random()
            p = p * u
        return int(k - 1)

    def random_string(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz     ' * 100000
        min = 50
        max = 200
        return ''.join(random.sample(alphabet,random.randint(min,max))).strip()
