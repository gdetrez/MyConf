from django.conf.urls.defaults import *
from myconf.settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myconf/', include('myconf.foo.urls')),
    (r'^$', 'homepage.views.index'),
    (r'^staff/$', 'people.views.staff'),
    (r'^staff/(?P<uname>\w+)/$', 'people.views.user'),
    (r'^notifications/$', 'notifications.views.index'),
    (r'^schedule/$', 'schedule.views.schedule'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
                       
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
)
