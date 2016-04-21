from .base import *


DEBUG = False

ADMINS = (
    ('Antonio M', 'antonio.mele@zenxit.com'),
)

ALLOWED_HOSTS = ['educa.com', 'www.educa.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '*****',
    }
}
