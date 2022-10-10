"""
Django settings for website_planning project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2@dh2p3xv8xthb!^7i!9k_&+-4iuyvt$bic24hqn@h5rcl$@mx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Local apps
    'apps.main',
    'apps.apis',
    'apps.users',
    'apps.gcia_plan.capex.dailyCapex',
    'apps.gcia_plan.capex.reportesCapex',
    'apps.gcia_plan.capex.serviciosCapex',
    'apps.gcia_plan.materiales.dailyMat',
    'apps.gcia_plan.materiales.reportesMat',
    'apps.gcia_plan.materiales.serviciosMat',
    'apps.gcia_plan.red.dailyRed',
    'apps.gcia_plan.red.reportesRed',
    'apps.gcia_plan.red.serviciosRed',
    'apps.gcia_calidad.reportesCali',
    'apps.gcia_ippc.reportesIPPC',
    'apps.gcia_rf.reportesRf',
    'apps.gcia_servfij.reportesServFij',
    'apps.gcia_tx.reportesTx',
    #Third party apps
    'rest_framework',
    'rest_framework.authtoken',
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

ROOT_URLCONF = 'website_planning.urls'


# Templates files (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

WSGI_APPLICATION = 'website_planning.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website_planning_database',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'db',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS =  (str(BASE_DIR.joinpath('static')),)


# Default primary key field type  --> Te creara el campo ID como primary key si no existe!! 
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# EMAIL - SMTP protocol
EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False


# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# LOGGING Stettings
LOGGING_DIR = '{}/website_planning/logs/' .format(BASE_DIR)
LOGGING = {
    'version': 1,
    # Mantenemos el resto de los loggers:
    'disable_existing_loggers': False,
    # Generamos filtros de estado de debug:
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # Diseñamos formateadores para los mensajes:
    'formatters': {
        'complete': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'generic': {
            'format': '[%(asctime)s] |%(levelname)s| %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S",
            'style': '%'
        }
    },
    # Generamos manejadores para los distintos tipos de mensajes:
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'generic'
        },
        # requests: para los mensajes del servidor:
        'requests': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'requests.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'generic',
        },
        # site: Para registrar los errores en el render de las variables de los templates.
        'site': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'template-rendering.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'complete',
        },
        # database: Registra las consultas en la base de datos [solo para debug]
        'database': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'database.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'complete',
        },
        # security: registra las operaciones sospechosas.
        'security': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'security.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'complete',
        },
        # generalbatch: Para registrar todos los mensajes, pero limita los logs a 15MB
        # Luego, fracciona el log en 10 partes segun backupCount.
        'generalbatch': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'general-batch.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'generic',
        },
    },
    # Ahora establecemos los loggers:
    'loggers': {
        # django.server: filtra los mensajes del servidor, pero en hasta 10 lotes de 15MB
        'django.server': {
            'handlers': ['requests', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # django.template: para los mensajes de renderizado de templates, pero en hasta 10 lotes de 15MB
        'django.template': {
            'handlers': ['site', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # django.db.backends: registra las querys a la base de datos, pero en hasta 10 lotes de 15MB
        'django.db.backends': {
            'handlers': ['database', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # django.security.csrf: registra errores csrf en formularios, pero en hasta 10 lotes de 15MB
        'django.security.csrf': {
            'handlers': ['security', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # django: registra todos los logs, pero en hasta 10 lotes de 15MB
        'django': {
            'handlers': ['generalbatch'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}