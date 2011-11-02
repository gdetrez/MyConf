from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:

    (r'^$', direct_to_template, {'template': 'home.djhtml'}),

    (r'^staff/$', 'myconf.apps.people.views.staff'),
    (r'^people/(?P<slug>[\w\d-]+)/$', 'myconf.apps.people.views.user'),

    (r'^schedule/', include('schedule.urls')),
    (r'^restaurants/', include('restaurants.urls')),

    (r'^map/$',
     direct_to_template, {'template': 'map.djhtml'}),

    (r'^information/$',
     direct_to_template, {'template': 'information/index.djhtml'}),
    (r'^information/getting-there/$',
     direct_to_template, {'template': 'information/gettingthere.djhtml'}),
    (r'^information/sleeping/$',
     direct_to_template, {'template': 'information/sleeping.djhtml'}),
    (r'^information/going-out/$',
     direct_to_template, {'template': 'information/goingout.djhtml'}),
    (r'^information/venue/$',
     direct_to_template, {'template': 'information/venue.djhtml'}),
    (r'^information/currency/$',
     direct_to_template, {'template': 'soon.djhtml'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
                       
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
