from timebound.settings import *

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

Debug = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'