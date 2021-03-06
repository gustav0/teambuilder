"""
Django settings for teambuilder project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@(#r+%ybuq(@ek95r^9&$2nj&o=hseazv_#n3q9&(wedk%xgl!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'teambuilder.apps.main',
    'teambuilder.apps.user',
    'teambuilder.apps.contact',
    'teambuilder.apps.login',
    'teambuilder.apps.lol',

    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'teambuilder.urls'

WSGI_APPLICATION = 'teambuilder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'teambuilder.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates')
)

LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'user.User'

ADMIN_MAIL = 'ingferrermiguel@gmail.com'

lol_api_key_0 = 'c645f0de-6970-4025-8ff9-5eecf24de2ed'
lol_api_key_1 = 'cc22a2c0-35d0-4bef-b178-deb4e925120a'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mdfingcisco@gmail.com'
EMAIL_HOST_PASSWORD = 'md0618096'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#setting up email server: python -m smtpd -n -c DebuggingServer localhost:1025