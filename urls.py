from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', direct_to_template, {'template': 'home.djhtml'}, name="home"),

    url(r'^staff/$', 'apps.people.views.staff', name="staff"),
    url(r'^people/(?P<slug>[\w\d-]+)/$', 'apps.people.views.user'),

    url(r'^schedule/api/', include('scheduleapi.urls', namespace="scheduleapi")),
    url(r'^schedule/', include('schedule.urls', namespace="schedule")),
    url(r'^cfp/', include('cfp.urls', namespace="cfp")),
    url(r'^restaurants/', include('restaurants.urls')),

    url(r'^map/$',
     direct_to_template, {'template': 'map.djhtml'}, name="map"),

    url(r'^information/$', direct_to_template,
     {'template': 'information/index.djhtml'}, name="information"),
    url(r'^information/getting-there/$', direct_to_template,
     {'template': 'information/gettingthere.djhtml'}, name="gettingthere"),
    url(r'^information/sleeping/$', direct_to_template,
     {'template': 'information/sleeping.djhtml'}, name="sleeping"),
    url(r'^information/going-out/$', direct_to_template,
     {'template': 'information/goingout.djhtml'}, name="goingout"),
    url(r'^information/venue/$', direct_to_template,
     {'template': 'information/venue.djhtml'}, name="venue"),
    url(r'^information/currency/$', direct_to_template,
     {'template': 'soon.djhtml'}, name="currency"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {
                'show_indexes' : True,
                }))
    urlpatterns += patterns('',
        url(r'^_uploads/(?P<path>.*)$', 'django.views.static.serve', {
                'show_indexes' : True,
                'document_root': settings.MEDIA_ROOT,
                }))
