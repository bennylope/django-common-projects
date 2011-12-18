import os
import sys


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Set the project root for cleanly setting media, static, and template
# directories
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))


# Put site specific apps in the apps folder
sys.path.append(os.path.join(PROJECT_ROOT, 'apps/'))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

gettext = lambda s: s

LANGUAGES = [
    ('en-us', 'English'),
]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collectedstaticfiles/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'cms_project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates/')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'sentry',
    'sentry.client',
    'compressor',
    'django_extensions',
    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'menus',
    'mptt',
    'sekizai',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'INFO',
            'class': 'sentry.client.handlers.SentryHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers':['sentry'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'joblister': {
            'handlers': ['sentry'],
            'propogate': True,
            'level': 'INFO',
        },
    }
}

# Registration/authentication settings
LOGIN_URL = '/admin/'
LOGIN_REDIRECT_URL = '/admin/'

# South migration settings
# South is used to manage database migrations. This is documented on the South
# webpage http://south.aeracode.org/docs/settings.html. The available settings
# include:
# SKIP_SOUTH_TESTS
# SOUTH_DATABASE_ADAPTER
# SOUTH_DATABASE_ADAPTERS
# MySQL STORAGE_ENGINE
# SOUTH_AUTO_FREEZE_APP
# SOUTH_TESTS_MIGRATE
# SOUTH_LOGGING_ON
# SOUTH_LOGGING_FILE
# SOUTH_MIGRATION_MODULES
# SOUTH_USE_PYC
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False


# Static file compression settings
#COMPRESS_CSS_FILTERS
#COMPRESS_JS_FILTERS
COMPRESS_OFFLINE = True
COMPRESS_OFFLINE_TIMEOUT = 71536000
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'MEDIA_URL': MEDIA_URL,
}
COMPRESS_OFFLINE_MANIFEST = 'manifest.json'


# Django-CMS settings
# The settings for Django-CMS include two very important settings for updating
# any templates: CMS_TEMPALTES and CMS_PLACEHOLDER_CONF. The former governs
# which templates are available to select from when creating a new page or
# editing an exisitng CMS page. The latter dictates what plugins can show up in
# which defined placeholders.
CMS_TEMPLATES = (
        ('cms/index.html', 'Index'),
)
#CMS_MEDIA_URL = "/static/cms/"
#CMS_MEDIA_PATH = "cms/"
#CMS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, "cms")
CMS_DEFAULT_LANGUAGE = 'en-us'
CMS_SEO_FIELDS = True
CMS_SOFTROOT = False
CMS_FLAT_URLS = False
CMS_PAGE_MEDIA_PATH = 'uploads'
CMS_MODERATOR = False
CMS_PERMISSION = False

CMS_APPHOOKS = ()

CMS_LANGUAGES = (
    ('fr', gettext('French')),
    ('de', gettext('German')),
    ('en', gettext('English')),
)

CMS_PLACEHOLDER_CONF = {
  'helloworld': {
      "plugins": ('TextPlugin',),
      "name": "Hello world"
  },
}
