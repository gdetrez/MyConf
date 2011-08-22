from django.conf.urls.defaults import *
from myconf.settings import MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:

    # (r'^myconf/', include('myconf.foo.urls')),
    (r'^$', direct_to_template, {'template': 'home.djhtml'}),

    (r'^staff/$', 'myconf.people.views.staff'),
    (r'^people/(?P<slug>[\w\d-]+)/$', 'myconf.people.views.user'),
    # (r'^notifications/$', 'notifications.views.index'),
    (r'^schedule/$', 'myconf.schedule.views.schedule'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
                       
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
)
