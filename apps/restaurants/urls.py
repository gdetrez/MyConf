from django.conf.urls.defaults import *

urlpatterns = patterns('apps.restaurants.views', 
    url(r'^$', 'list', name="restaurants"),
)
