from django.conf.urls.defaults import *

urlpatterns = patterns('scheduleapi.views',
    url(r'^now_and_next/$', 'now_and_next'),
)
