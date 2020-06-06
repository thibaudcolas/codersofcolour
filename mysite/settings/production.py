import os
import dj_database_url
from .base import *


env = os.environ.copy()

SECRET_KEY = env['SECRET_KEY']
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
DEBUG = False

try:
   from .local import *
except ImportError:
   pass