from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=['*']))

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('NAME_DB'),
        'USER': env.str('USER_DB'),
        'PASSWORD': env.str('PASSWORD_DB'),
        'HOST': env.str('HOST_DB'),
        'PORT': env.int('PORT_DB')
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR.parent, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR.parent, 'static'),)

# email
EMAIL_BACKEND = env.str('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST = env.str('EMAIL_HOST', default='your.email.host')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default='your email host user')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default='your email host password')
EMAIL_PORT = env.int('EMAIL_PORT', default=2525)