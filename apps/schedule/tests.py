"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import *
from .utils import *
from datetime import *


class ConcurrentSessionsTestCase(TestCase):
    """ 
    Test the function that return the concurent sessions given a reference
    session.

    It starts by filling the database with the following sessions:
    
           t1   t2   t3   t4   t5   t6   t7   t8   t9   t10
    |------|----|----|----|----|----|----|----|----|----|---------------> time
    s                |==============|           reference session
    s0     |====|                               starts and ends before
    s1     |=========|                          starts before, ends at start
    s2     |==============|                     starts before, ends during
    s3     |========================|           starts before, same end
    s4     |=============================|      starts before, ends after
    s5               |====|                     same start, ends during
    s6               |==============|           same start and same end
    s7               |===================|      same start, ends after
    s8                    |====|                start during, ends during
    s9                    |=========|           start during, same end
    s10                   |==============|      start during, ends after
    s11                             |====|      starts at end, ends after
    s12                                  |====| starts and ends after
    
    According to this, and relative to s:
    - s2, s3, s4, s5, s6, s7, s8, s9, s10 are concurent
    """
    def setUp(self):
        t0 = datetime.fromtimestamp(0)
        t = [t0 + timedelta(minutes=i*10) for i in range (0,10)]
        for i,times in enumerate([ (1, 2), (1, 3), (1, 4), (1, 6), (1, 7),
                                   (3, 4), (3, 6), (3, 7),
                                   (4, 5), (4, 6), (4, 7),
                                   (6, 7), (7, 8) ]):
            ts = TimeSlot.objects.create(begin = t[times[0]],end = t[times[1]])
            Session.objects.create(title = "s" + str(i), time_slot = ts)

        ts = TimeSlot.objects.get(begin = t[3], end = t[6])
        Session.objects.create(title = "s", time_slot = ts).save()

    def test_get_concurrent_sessions(self):
        g = Session.objects.filter(title__in=["s2", "s3", "s4", "s5",
                                           "s6", "s7", "s8", "s9", "s10"])
        t = get_concurrent_sessions(Session.objects.get(title="s"))
        self.failUnlessEqual(set(g), set(t))
    

class FollowingSessionsTestCase(TestCase):
    """ 
    Test the function that return the following sessions given a reference
    session and the maximum number of limit in which the following session 
    are supposed to start.

    It starts by filling the database with the following sessions:
    
           t1   t2   t3   t4   t5   t6   t7   t8   t9   t10
    |------|----|----|----|----|----|----|----|----|----|---------------> time
    s                |====|           reference session
    s1     |====|
    s2          |====|
    s3               |====|
    s4                    |====|
    s5                         |====|
    s6                              |====|
    s7                                   |====|
    sx          |====| <-- different day
    
    According to this, depending on the time span and relative to s:
    s4, s5, s6 and s7 can be returned
    """
    def setUp(self):
        t0 = datetime.fromtimestamp(0)
        t = [t0 + timedelta(minutes=i*10) for i in range (0,10)]
        for i in range(1,8):
            ts = TimeSlot.objects.create(begin = t[i],end = t[i+1])
            Session.objects.create(title = "s" + str(i), time_slot = ts)

        ts = TimeSlot.objects.get(begin = t[3], end = t[4])
        self.session = Session.objects.create(title = "s", time_slot = ts)

        ts = TimeSlot.objects.create(begin=t0 + timedelta(days=1),
                                     end=t0 + timedelta(days=1, minutes=10) )
        Session.objects.create(title = "sx", time_slot = ts)
        
    def test_get_following_sessions_0_minutes(self):
        # 0 minutes
        g = Session.objects.filter(title__in=["s4"])
        t = get_following_sessions(self.session, 0)
        self.failUnlessEqual(set(g), set(t))
    def test_get_following_sessions_10_minutes(self):
        # 10 minutes
        g = Session.objects.filter(title__in=["s4", "s5"])
        t = get_following_sessions(self.session, 10)
        self.failUnlessEqual(set(g), set(t))
    def test_get_following_sessions_30_minutes(self):
        # 30 minutes
        g = Session.objects.filter(title__in=["s4", "s5", "s6", "s7"])
        t = get_following_sessions(self.session, 30)
        self.failUnlessEqual(set(g), set(t))
    def test_get_following_sessions_1_year(self):
        # 365 * 24 * 60 minutes (a year)
        g = Session.objects.filter(title__in=["s4", "s5", "s6", "s7", "sx"])
        t = get_following_sessions(self.session, 365 * 24 * 60)
        self.failUnlessEqual(set(g), set(t))
    

class NextSessionsInRoomTestCase(TestCase):
    """ 
    Test the function that return the next sessions in the same room given 
    a reference session and the maximum number sessions desired.

    It shouldn't return session on a different day.

    It starts by filling the database with the following sessions:
    
           t1   t2   t3   t4   t5   t6   t7   t8   t9   t10
    |------|----|----|----|----|----|----|----|----|----|---------------> time
    ROOM 1
    s1     |====|
    s2          |====|
    s3               |****|  <--- Reference session
    s4                    |====|
    s5                         |====|
    s6                              |====|
    s7                                   |====|
    s8     |====| <-- next day
    ROOM2
    s9                         |====|
    
    According to this and relative to s:
    s4, s5, s6 and s7 can be returned
    """
    def setUp(self):
        t0 = datetime.fromtimestamp(0)
        room1 = Room.objects.create(name="ROOM1")
        room2 = Room.objects.create(name="ROOM2")
        t = [t0 + timedelta(minutes=i*10) for i in range (0,10)]
        for i in range(1,8):
            ts = TimeSlot.objects.create(begin = t[i],end = t[i+1])
            Session.objects.create(title = "s" + str(i),
                                   time_slot = ts, 
                                   room = room1)

        ts = TimeSlot.objects.create(begin=t0 + timedelta(days=1),
                                     end=t0 + timedelta(days=1, minutes=10) )
        Session.objects.create(title = "s8", time_slot = ts, room=room1)

        ts = TimeSlot.objects.get(begin = t[5], end = t[6])
        Session.objects.create(title = "s9", time_slot = ts, room=room2)

        ts = TimeSlot.objects.get(begin = t[3], end = t[4])
        self.session = Session.objects.get(time_slot = ts, room=room1)
        
    def test_get_next_1_sessions(self):
        # 1 session minutes
        g = Session.objects.filter(title__in=["s4"])
        t = get_next_n_sessions_in_room(self.session, 1)
        self.failUnlessEqual(set(g), set(t))
    def test_get_next_2_sessions(self):
        # 2 session minutes
        g = Session.objects.filter(title__in=["s4", "s5"])
        t = get_next_n_sessions_in_room(self.session, 2)
        self.failUnlessEqual(set(g), set(t))
    def test_get_next_3_sessions(self):
        # 3 session minutes
        g = Session.objects.filter(title__in=["s4", "s5", "s6"])
        t = get_next_n_sessions_in_room(self.session, 3)
        self.failUnlessEqual(set(g), set(t))
    def test_get_next_4_sessions(self):
        # 4 session minutes
        g = Session.objects.filter(title__in=["s4", "s5", "s6", "s7"])
        t = get_next_n_sessions_in_room(self.session, 4)
        self.failUnlessEqual(set(g), set(t))
    def test_get_next_5_sessions(self):
        # 5 session minutes
        g = Session.objects.filter(title__in=["s4", "s5", "s6", "s7"])
        t = get_next_n_sessions_in_room(self.session, 5)
        self.failUnlessEqual(set(g), set(t))

    
