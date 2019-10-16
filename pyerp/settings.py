"""
Django settings for pyerp project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Standard Library
import logging
import os

# Django Library
from django.utils.translation import ugettext_lazy as _

_logger = logging.getLogger(__name__)


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(filename)s:%(lineno)d - %(message)s')
logging.debug('hello world!')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(5u_8%)7z-9t#pxxg8@$bt99rr)m6*ceuqf4-ic79-mmd8=^mw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'www.pyerp.cl', 'pyerp.cl']


# Application definition

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Third-Party Apps
    'dynamic_formsets',
    'crispy_forms',
    'dal',
    'dal_select2',
    'bootstrap4',
    'tempus_dominus',
    'rest_framework',
    'rest_framework.authtoken',

    # Local Apps
    'apps.base',
]


# ========================================================================== #
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)


# ========================================================================== #
# Se instalan todas las app que estan como plugins en tiempo de arranque
# Copiar en localsettings.py
with open('%s/installed_apps.py' % BASE_DIR, 'r') as ins_apps_file:
    for line in ins_apps_file.readlines():
        INSTALLED_APPS += [line.strip()]


# ========================================================================== #
# Para la localizacion i18n de los componentes de fecha y hora de bootstrap

TEMPUS_DOMINUS_LOCALIZE = True


# ========================================================================== #
""" Esta configuración hace disponible todas esta variables en cualquier
plantilla
"""
APP_NAME = 'PyERP'
SLOGAN = _('We make your Day Easy')
PREFIX = 'Py'
SUFIX = 'ERP'
VERSION = '1.0'
INITIAL_A = 'P'
INITIAL_B = 'E'

SETTINGS_EXPORT = [
    'APP_NAME',
    'SLOGAN',
    'PREFIX',
    'SUFIX',
    'VERSION',
    'INITIAL_A',
    'INITIAL_B'
]

# ========================================================================== #
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyerp.urls'

# ========================================================================== #
""" Esta es la clave para el recaptcha de google, hay que busca una para el
proyecto
"""
GOOGLE_RECAPTCHA_SECRET_KEY = '6LevF1gUAAAAAPn3z8EswCgIk1S_jLKYdf4s62B9'

# ========================================================================== #
"""Cada procesor de contexto de los templates tiene su razon de ser para mayor
detalle: https://docs.djangoproject.com/en/2.2/ref/templates/api/
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',

            ],
        },
    },
]

WSGI_APPLICATION = 'pyerp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# ========================================================================== #
""" Esta configuración define el modelo personalizado para auth.user. Tambien
establece las rutas para algunas funciones.
"""
AUTH_USER_MODEL = 'base.PyUser'
LOGIN_URL = 'PyUser:login'
LOGIN_REDIRECT_URL = 'base:home'
LOGOUT_REDIRECT_URL = 'PyUser:login'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# ========================================================================== #
""" EL tempo de validez de los token de activación de la cuenta del usuario y
recuperacion de contraseña del usuario.
"""
PASSWORD_RESET_TIMEOUT_DAYS = 1


# ========================================================================== #
""" Este bloque contiene toda la configuración para la loclización
"""
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# def gettext(cadena):
#     '''  "dummy" gettext() function
#     '''
#     return cadena

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Santiago'
# Restricts languages
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish'))
]
# Where Django looks for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ========================================================================== #
""" Este bloque es para la configuración de los estaticos y los archivos de
imagens
"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


# ========================================================================== #
""" En este bloque se debe configurar el servidor de correo que utilizará
Django para enviar correos.
"""
# During development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# No borrar esto, si falla importando, entra en el try y simplemente muestra el
# warning, esto porque en producción SI EXISTE EL LOCALSETTINGS, es buena
# practica tener un localsettings para configuraciones locales, y no meter claves
# ni cosas delicadas en éste settings.py
try:
    from .localsettings import *
except ImportError:
    _logger.warning('No hay localsettings, trabajando con settings global.')


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', )
}
