from django.conf.urls.defaults import *

urlpatterns = patterns('myconf.apps.restaurants.views', 
    (r'^$', 'list'),
)
