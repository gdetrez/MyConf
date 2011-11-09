# -*- coding: utf-8 -*-
# Django settings for myconf project.

import sys, os
from os.path import join
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT = PROJECT_ROOT
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'devdb.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

ADMINS = (
    ('Grégoire', 'gdetrez@crans.org'),
)

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'people.Profile'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Stockholm'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/_uploads/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT,'_uploads/')

# URL that handles the static files served from STATIC_ROOT and collected by 
# the collectstatic managment command. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://static.lawrence.com", "http://example.com/static/"
STATIC_URL = '/static/'

# Absolute path to the directory where static files are collected.
# Example: "/home/static/media.lawrence.com/"
STATIC_ROOT = os.path.join(ROOT, "_static/")

# Extra directories where static files needs to be harvested
STATICFILES_DIRS = (
    ("style", os.path.join(ROOT, "style/")),
    ("", os.path.join(ROOT, "static/")),
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fghiweuhglkadjflerigha#D%G4d#f%&Gofpqeiugb123456h½!"#eufhqei'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT, "templates/"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'myconf.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Manage the static files
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    # Add markup
    'django.contrib.markup',

    # Add tagging
    'taggit',
    # add thumbnails
    'sorl.thumbnail',
    
    # MyConf apps
    'apps.people',
    #'notifications',
    #'simulator',
    'apps.schedule',
    'apps.restaurants',
    'apps.colors',
    'apps.signup',
    'apps.map',
    'apps.scheduleapi'
)

THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_FORMAT = "PNG"

try:
    # import local settings (non commited to git)
    from localsettings import *
except ImportError:
    pass

