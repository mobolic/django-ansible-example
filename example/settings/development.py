# Django settings for a development environment.
from .base import *     # noqa


DEBUG = True
# Let's not send email while we are doing local testing.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
