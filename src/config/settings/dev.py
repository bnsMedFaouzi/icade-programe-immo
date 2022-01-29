"""
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

For more information on production settings
https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
"""
from .base import *
from os import getenv

# ### DEBUG CONFIGURATION ###########################
DEBUG = True

# ### HOST CONFIGURATION ##############################
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '0.0.0.0,').split(',')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(PROJECT_ROOT, 'db.sqlite3')),
    }
}
