"""
Django settings for silvanapp project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

#Twitter Authentification
from twython import Twython
twitter = Twython('hCkbdXZwdoFoIJsQqANRQ', 'mccOHaIdUEH8hsLoX0VtYe3sjlgfaX2RiChHT02rg','163400534-6PVteKAIQZVGmU2drQZJ0huwU2nBYS0UWbY7qAxW', 'pP7pa4UH0klP8JlOFmYBL5JhlJkLxmZ0qcreSohjulsig')

# Email setup
EMAIL_USE_TLS = True
EMAIL_HOST = 'pegasus.uberspace.de'
EMAIL_HOST_USER = 'hallo@silvanadrian.ch'
EMAIL_HOST_PASSWORD = 'silvan%%1993'
EMAIL_PORT = 587

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = 'z^+#1vz3v=ijfdk)_88!_)a(t3ypn#p6jo!8tttw1!7y2*m+3v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

#SITE_ID = 1

ALLOWED_HOSTS = ['silvanadrian.ch','www.silvanadrian.ch']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
                  #'django.contrib.sites',
                  #'django.contrib.flatpages',
    'blog',
    'projects',
    'south',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'silvanapp.urls'

WSGI_APPLICATION = 'silvanapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'silvanapp.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

#STATICFILES_DIRS = (
 #  '/var/www/virtual/svenne/django.silvanadrian.ch/static/',)


STATIC_URL = '/static/'

MEDIA_ROOT = '/home/svenne/html/'

MEDIA_URL = '/media/'
