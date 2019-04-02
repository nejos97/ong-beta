from ong.settings import *
import dj_database_url

TEMPLATE_DEBUG = False

SECRET_KEY = "xa@%e5&m449$0($##&*hcywjib5(t_u)r*gt5dtc3@pjlfls8h"

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
