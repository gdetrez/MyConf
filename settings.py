# -*- coding: utf-8 -*-
# Django settings for myconf project.

# import local settings (non commited to git)
from localsettings import *

#DEBUG = True                                      # defined in localsettings
#TEMPLATE_DEBUG = DEBUG                            # defined in localsettings

ADMINS = (
    ('Grégoire', 'gdetrez@crans.org'),
)

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'people.Profile'

# XMPP server configuration.
#XMPP_PUBSUB_HOST = "pubsub.zjyto.net"
#XMPP_JID = "myconf-django@zjyto.net"
#XMPP_PASSWORD = "0000"

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
MEDIA_ROOT = ROOTDIR + '_uploads/'

# URL that handles the static files served from STATIC_ROOT and collected by 
# the collectstatic managment command. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://static.lawrence.com", "http://example.com/static/"
STATIC_URL = '/static/'

# Absolute path to the directory where static files are collected.
# Example: "/home/static/media.lawrence.com/"
STATIC_ROOT = ROOTDIR + "_static/"

# Extra directories where static files needs to be harvested
STATICFILES_DIRS = (
    ("style", ROOTDIR + "/style/"),
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
    ROOTDIR + "templates/"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
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
    
    # MyConf apps
    'myconf.people',
    #'notifications',
    #'simulator',
    'myconf.schedule',
    'myconf.restaurants',
    'myconf.colors',
)
