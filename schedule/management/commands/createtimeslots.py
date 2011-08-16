from schedule.models import TimeSlot
from django.core.management.base import BaseCommand, CommandError
import time, math, random, sys
from optparse import make_option
import datetime

combine = datetime.datetime.combine

DEFAULT_LENGTH = datetime.timedelta(minutes=45)

RED = '\033[01;31m%s\033[00m'
GREEN = '\033[01;32m%s\033[00m'
BOLD = '\033[01;1m%s\033[00m'

class InputError(Exception):
    pass

class EOD(Exception):
    # EOD = End Of Day
    pass

class Command(BaseCommand):
    args = '<day 1 (aaaa-mm-dd), day 2...>'
    help = 'Helper to create timeslots'
    option_list = BaseCommand.option_list + (
        make_option('--reset',
            action='store_true',
            dest='reset',
            default=False,
            help='Remove old timeslots before'),
        )

    def handle(self, *args, **options):
        timeslots = []
        parse_date = lambda s: datetime.datetime.strptime(s, "%Y-%m-%d").date()
        dates = map(parse_date, args)
        for i, day in enumerate(dates):
            print GREEN % "Day %d: %s" % (i+1, day)
            if len(timeslots) > 0:
                same = None
                while not same or same.lower() not in ["y","n"]:
                    same = raw_input("Use the same timeslots for day %d [y/n]? " % (i+1))
                if same.lower() in ['', 'y']:
                    def update (tss):
                        begin, end = tss
                        begin = combine(day, begin.time())
                        end = combine(day, end.time())
                        return (begin, end)
                    day_ts = map(update, timeslots[-1])
                    timeslots.append(day_ts)
                    continue

            day_ts = []
            begin, end = None, None
            while True:
                try:
                    begin = self.read_time("Slot %d, begin Time" % (len(day_ts) + 1), end)
                    begin = combine(day, begin)
                    end = self.read_time("End Time", (begin + DEFAULT_LENGTH).time())
                    day_ts.append((begin, combine(day,end)))
                except EOD:
                    break
            timeslots.append(day_ts)

        print 
        print BOLD % "** Summary **"
        for i,day in enumerate(dates):
            print GREEN % "Day %d: %s" % (i+1, day)
            for begin,end in timeslots[i]:
                print "\t%s - %s (%s)" % (
                    begin.time(), end.time(), (end - begin))
        save = None
        while not save or  save.lower() not in ["y","n", '']:
            save = "y"
            save = raw_input("save those time slots [y/n]? ")
        if save.lower() in ['', 'y']:
            print "Saving..."
            if options['reset']:
                TimeSlot.objects.all().delete()
            
            for l in timeslots:
                for begin,end in l:
                    ts = TimeSlot()
                    ts.begin = begin
                    ts.end = end
                    ts.save()

    def read_time(self, prompt, default = None):
        if default:
            prompt = "%s [%s] ? " % (prompt, default.strftime("%H:%M"))
        else:
            prompt ="%s? " % (prompt)
        while True:
            try:
                answer = raw_input(prompt)
                if default and answer == '':
                    return default
                if answer.lower() == "eod" or answer.lower() == "end of day":
                    raise EOD()
                return self.parse_time(answer)
            except InputError, e:
                print RED % e

    def parse_time(self, s):
        try:
            if ':' in s:
                values = map(int, s.split(":"))
            elif len(s) > 2:
                values = map(int, [s[:-2], s[-2:]])
            else: 
                values = [int(s)]
        except ValueError:
            raise InputError("Wrong format, use hh:mm or 'end' to finish the day.")
        try:
            return datetime.time(*values)
        except ValueError, e:
            raise InputError(e)
        
