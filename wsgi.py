import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'cmuhappyhours')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'cmuhappyhours.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()