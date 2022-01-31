"""
Django base settings for social network project.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from .base import *
from os import getenv

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('POSTGRES_DATABASE', ''),
        'USER': getenv('POSTGRES_USER', ''),
        'PASSWORD': getenv('POSTGRES_PASSWORD', ''),
        'HOST': getenv('POSTGRES_HOST', ''),
        'PORT': getenv('POSTGRES_PORT', ''),
    }
}