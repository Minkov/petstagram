import os

from django.urls import reverse_lazy

DEBUG = os.environ.get("DEBUG", "1") == "1"


def get_production_settings():
    return [
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


def get_local_settings():
    return []


AUTH_PASSWORD_VALIDATORS = get_local_settings() if DEBUG else get_production_settings()

AUTH_USER_MODEL = 'accounts.PetstagramUser'

LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGIN_URL = reverse_lazy("signin user")
LOGOUT_REDIRECT_URL = reverse_lazy("index")
