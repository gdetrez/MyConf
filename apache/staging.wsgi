import os
import sys
import site

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
site_packages = os.path.join(os.path.dirname(PROJECT_ROOT), 'env/lib/python2.6/site-packages')
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'fscons.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
