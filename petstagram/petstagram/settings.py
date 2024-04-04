import os
from pathlib import Path

from django.urls import reverse_lazy
from petstagram.setting_configs.db_settings import DATABASES

# `BASE_DIR` should always point to the `manage.py` directory
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-h80@s92%21e^5e+_yib)m3h(b+y+lq#czu**g(+jz8!$^0c+4y"

DEBUG = os.environ.get("DEBUG", "1") == "1"
# DEBUG=0 in environment
# DEBUG="0" in python, and "0" is truthy

# Example env variable: `ALLOWED_HOSTS=localhost 127.0.0.1`
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(" ")
CSRF_TRUSTED_ORIGINS = [f'https://{host}' for host in ALLOWED_HOSTS]

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "whitenoise.runserver_nostatic",

    # Project apps
    "petstagram.common",
    "petstagram.accounts",
    "petstagram.photos",
    "petstagram.pets",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "petstagram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "petstagram.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = ()

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# URL prefix in the client
STATIC_URL = "/static/"

# Directories on the file system
STATICFILES_DIRS = (
    BASE_DIR / "staticfiles",
)

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

MEDIA_ROOT = BASE_DIR / 'mediafiles'

MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'accounts.PetstagramUser'

LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGIN_URL = reverse_lazy("signin user")
LOGOUT_REDIRECT_URL = reverse_lazy("index")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "in-v3.mailjet.com"
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_HOST_USER = "2d2d4c2df3e037dc539ecc2c12e749fc"
EMAIL_HOST_PASSWORD = "348887433b3164837ac1726db61b217d"
