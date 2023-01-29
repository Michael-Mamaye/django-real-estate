from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        "USER":env("POSTGRES_USER"),
        "PASSWORD":env("POSTGRES_PASSWORD"),
        "HOST":env("PG_HOST"),
        "PORT":env("PG_PORT"),
    }
}