# This settings file is for a production environment

from .base import *

# Django will throw an error without a secret key. You should generate one
# yourself and include it here. It should not be shared.
SECRET_KEY = None

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except ImportError:
    pass
