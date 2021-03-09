"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ye*j6l^@8xec5_*o0xvx1g%n@tzns2r^zwt)eayma7b#p&d072'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['disability45.herokuapp.com','africa-disability-alliance.herokuapp.com','127.0.0.1',]
# heroku
# django_heroku.settings(locals())
# Application definition

INSTALLED_APPS = [
    #  'admin_interface',
    # # 'flat_responsive', # only if django version < 2.0
    # # 'flat', # only if django version < 1.9
    # 'colorfield',
    # 'admin_interface',
    # 'flat_responsive', # only if django version < 2.0
    # 'flat', # only if django version < 1.9
    # 'colorfield',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #social networks
    # 'social_django',

    #my custom apps
    'account',
    'post',
    'survey',
    'tutor',
    'contact',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
    # 'social_django.middleware.SocialAuthExceptionMiddleware',  # <-- Here
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'social_django.context_processors.backends',  # <-- Here
                # 'social_django.context_processors.login_redirect', # <-- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")), #BASE_DIR / 'db.sqlite3',
    }
}

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# AUTH_USER_MODEL = 'account.UserProfile'
# AUTH_USER_MODEL = 'account.UserProfile'
AUTH_USER_MODEL = 'account.Account'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "/static/")
# ]

STATICFILES_DIRS = [
    BASE_DIR / "static",

]

MESSAGE_TAGS = {
    messages.DEBUG : 'alert-info',
    messages.INFO : 'alert-info',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
    messages.ERROR : 'alert-danger',
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# X_FRAME_OPTIONS='SAMEORIGIN' # only if django version >= 3.0

# #SOCIAL LOGIN
# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.facebook.FacebookOAuth2',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.github.GithubOAuth2',

#     'django.contrib.auth.backends.ModelBackend',
# )


# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'profile'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# SESSION_COOKIE_AGE = 5 # one hour in seconds
SESSION_EXPIRE_SECONDS = 60*45  # 1 hour
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute
SESSION_TIMEOUT_REDIRECT = 'logout'
#SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mcm96m@gmail.com'
EMAIL_HOST_PASSWORD = 'mulalo96'
DEFAULT_FROM_EMAIL = 'Africa Disability Alliance Team <noreply@disabilityalliance.org>'
django_heroku.settings(locals())
