import os
import sys
import site

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
APPS_ROOT = os.path.join(PROJECT_ROOT, 'apps')
site_packages = os.path.join(PROJECT_ROOT, 'env/lib/python2.6/site-packages')
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'myconf'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'myconf.fscons_org.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
