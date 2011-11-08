from django.conf.urls.defaults import *

urlpatterns = patterns('schedule.views',
    url(r'^$', 'schedule', name='schedule'),
    url(r'^session/(?P<pk>\d+)/$', 'session', name="session"),
    url(r'^track/(?P<slug>[\w\d-]+)/$', 'track', name="track"),
    url(r'^tag/(?P<slug>[\w\d-]+)/$', 'tag', name="tag"),
    url(r'^schedule.xml$', 'xml', name="schedulexml"),
)
urlpatterns+= patterns('signup.views',
    url(r'^session/(?P<session_pk>\d+)/signup/$', 'signup'),
)
