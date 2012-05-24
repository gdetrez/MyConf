from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('cfp.views',
    url(r'^$', direct_to_template, {'template': 'cfp/cfp.djhtml'}, name="cfp"),
    url(r'^submit/$', 'submit', name="submit"),
    url(r'^edit/$', 'edit', name="edit"),
    url(r'^accessibility/$', direct_to_template, {'template': 'cfp/accessibility_pledge.djhtml'}, name="accessibility"),
)
