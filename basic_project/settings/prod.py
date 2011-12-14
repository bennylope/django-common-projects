# This settings file is for a production environment

from .base import *

# Django will throw an error without a secret key. You should generate one
# yourself and include it here. It should not be shared.
SECRET_KEY = None

DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except ImportError:
    pass
