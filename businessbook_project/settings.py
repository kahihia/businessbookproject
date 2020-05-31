"""
Django settings for businessbook_project project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__mjzwl^t$&czf_v+mchp^gw7fig9v8x!$6z_taitg$8$_roqd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','profiteebd.com','www.profiteebd.com','3.130.72.33','www.businessbook.ltd','businessbook.ltd']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'dashboard.apps.DashboardConfig',
    #external apps area
    'phonenumber_field',
    'django_countries',
    'django_email_verification',
    'django_crontab',

    #end of external apps area
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'businessbook_project.urls'

AUTH_USER_MODEL='accounts.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'businessbook_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'businessbook',
        'HOST':'127.0.0.1',
        'USER':'shakil',
        'PASSWORD':'Shakil121'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/





STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'staticfiles')]

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

'''
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = '<admin@webheavenit.com>'
EMAIL_HOST_PASSWORD = '<cV1PYSn7yc7v>'
DEFAULT_FROM_EMAIL= '<admin@webheavenit.com>'

'''





EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True

EMAIL_PORT = 587
EMAIL_HOST_USER = 'shakil4cash@gmail.com'
EMAIL_HOST_PASSWORD = 'wjkhjgdjhqsqqynx'

EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_ADDRESS = 'shakil4cash@gmail.com'
EMAIL_PASSWORD = 'wjkhjgdjhqsqqynx'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'accounts/email-confirmation-mail.html'
EMAIL_PAGE_TEMPLATE = 'accounts/activation-conf.html'
EMAIL_PAGE_DOMAIN = '127.0.0.1:8000'
EMAIL_MODEL_ADMIN = False # the default value is False
DEFAULT_FROM_EMAIL= 'shakil4cash@gmail.com'

'''
EMAIL_SERVER = 'smtp.zoho.com'
EMAIL_ADDRESS = 'admin@webheavenit.com'
EMAIL_PASSWORD = 'cV1PYSn7yc7v'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'accounts/email.html'
EMAIL_PAGE_TEMPLATE = 'accounts/activation-conf.html'
EMAIL_PAGE_DOMAIN = '127.0.0.1'
EMAIL_MODEL_ADMIN = False # the default value is False
DEFAULT_FROM_EMAIL= 'admin@webheavenit.com'
'''


CRONJOBS = [
    ('59 23 * * *', 'dashboard.cron.adpack_daily_update')
]