# -*- coding: utf-8 -*-
# Django settings for myconf project.

from settings import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Absolute path to the root of the project.
# i.e. the folder where this file is.
ROOTDIR="/home/gdetrez/Sources/MyConf/myconf/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'development.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
