import os

from dotenv import load_dotenv
from configurations.wsgi import get_wsgi_application

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "like_otus.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()
