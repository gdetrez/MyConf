from django.conf.urls.defaults import *

urlpatterns = patterns('schedule.views',
    (r'^$', 'schedule'),
    (r'^session/(?P<pk>\d+)/$', 'session'),
    (r'^session/(?P<session_pk>\d+)/signup/$', 'signup'),
    (r'^track/(?P<slug>[\w\d-]+)/$', 'track'),
    (r'^tag/(?P<slug>[\w\d-]+)/$', 'tag'),    
)
