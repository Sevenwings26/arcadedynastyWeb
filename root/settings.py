"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 4.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# from environ import Env
import environ
env = environ.Env()
environ.Env.read_env()
import dj_database_url


ENVIRNOMENT = env('ENVIRONMENT', default="production")
ENVIRNOMENT = "production"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRNOMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'arcadedynastyweb.onrender.com']
# ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(',')

CSRF_TRUSTED_ORIGINS = [ "https://arcadedynastyweb.onrender.com" ]

# Application definition

INSTALLED_APPS = [
    "applications",
    "account",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # created app
    'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',  # Optional for social auth
    
    #installations
    "tailwind",
    "theme",
    'django_browser_reload',
    'widget_tweaks',
    "cloudinary_storage",
    "cloudinary",
]

AUTH_USER_MODEL = 'account.User'

# SITE_ID = 1

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
    'localhost',
]
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
     "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "root.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "root.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if ENVIRNOMENT == 'development':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(env('EXTERNAL_DATABASE_URL'))
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR / 'static')
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media files 
# Define the base URL for serving media files
MEDIA_URL = 'media/'

if ENVIRNOMENT == "development":
    # Specify the directory where media files are stored
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': env('CLOUDINARY_URL'),
        'CLOUDINARY_CLOUD_NAME' : env('CLOUDINARY_CLOUD_NAME'),
        'CLOUDINARY_API_KEY': env('CLOUDINARY_API_KEY'),
     'CLOUDINARY_API_SECRET':env('CLOUDINARY_API_SECRET'),
    }


# mail = os.environ.get("EMAIL")
# mail_pass = os.environ.get("EMAIL_PASSWORD")
# EMAIL_HOST = 'smtp.mail.outlook.com'


# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL')
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = env('EMAIL')
ACCOUNT_EMAIL_SUBJECT_PREFIX = " "