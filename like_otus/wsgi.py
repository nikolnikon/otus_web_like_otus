"""
WSGI config for like_otus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
from configurations.wsgi import get_wsgi_application

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "like_otus.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()
