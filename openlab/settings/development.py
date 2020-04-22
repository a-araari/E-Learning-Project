from .base import *


DEBUG = True
ALLOWED_HOSTS = []


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testsite_app'
EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'


SECRET_KEY = '7snund80^35%@i9%!wobh_0vj9nbbdjak^^(j3@8hgk8-5((ec'