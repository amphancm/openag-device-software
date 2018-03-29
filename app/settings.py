"""
Django settings for brain project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'flnh=1!tsz^4&grtw&0$2&6#n*@aybhg-vdpa-i1rc&pyv$+9c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
    'device'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'app/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'openag_brain',
        'USER': 'openag',
        'PASSWORD': 'openag',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard_console': {
            'format' : "%(levelname)s %(name)s: %(message)s",
        },
        'standard_file': {
            'format' : "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'device_console': {
            'format' : "%(levelname)s %(console_name)s: %(message)s",
        },
        'device_file': {
            'format' : "[%(asctime)s] %(levelname)s %(file_name)s: %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'app_console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard_console',
        },
        'app_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.dirname(BASE_DIR) + "/log/app.log",
            'formatter': 'standard_file',
        },
        'device_console': { 
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'device_console',
        },
        'device_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.dirname(BASE_DIR) + "/log/device.log",
            'formatter': 'device_file',
        },

    },
    'loggers': {
        'app': {
            'handlers': ['app_console', 'app_file'],
            'level': 'INFO',
        },
        'device': {
            'handlers': ['device_console', 'device_file'],
            'level': 'INFO',
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'