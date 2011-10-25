from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:

    # (r'^myconf/', include('myconf.foo.urls')),
    (r'^$', direct_to_template, {'template': 'home.djhtml'}),

    (r'^staff/$', 'myconf.apps.people.views.staff'),
    (r'^people/(?P<slug>[\w\d-]+)/$', 'myconf.apps.people.views.user'),
    # (r'^notifications/$', 'notifications.views.index'),
    (r'^schedule/$', 'myconf.apps.schedule.views.schedule'),
    (r'^schedule/session/(?P<pk>\d+)/$', 'myconf.apps.schedule.views.session'),
    (r'^schedule/session/(?P<session_pk>\d+)/signup/$',
     'myconf.apps.signup.views.signup'),
    (r'^schedule/track/(?P<slug>[\w\d-]+)/$', 'myconf.apps.schedule.views.track'),
    (r'^schedule/tag/(?P<slug>[\w\d-]+)/$', 'myconf.apps.schedule.views.tag'),
    
    (r'^restaurants/$', 'myconf.apps.restaurants.views.list'),

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
    (r'^information/accessibility/$',
     direct_to_template, {'template': 'information/accessibility.djhtml'}),

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
