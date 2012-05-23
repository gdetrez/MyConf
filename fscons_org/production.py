# -*- coding: utf-8 -*-
# Django settings for myconf project.

from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fscons_myconf',
        'USER': 'fscons_myconf',
        'PASSWORD': 'TifJe9quank',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

