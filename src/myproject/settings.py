import os
from pathlib import Path
from django.contrib.messages import constants as messages
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-g%1t@+d-mh0192nue4j(@1f-rw_jqc207evnn4zauox&bn!3-k'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # My apps
    'datalist',
    
    # default app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'crispy_forms',
    
]

CRISPY_TEMPLATE_PACK= "bootstrap4"
# AUTH_USER_MODEL = 'accounts.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "",
    #     "USER": "postgres",
    #     "PASSWORD": "",
    #     "HOST": "localhost",
    #     "PORT": "9001",
    # }
}

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
FORCE_STATIC_FILE_SERVING = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject/static')
]

# Media settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# MESSAGES
MESSAGE_TAGS = {messages.ERROR: "danger"}

# EMAIL CONFIG
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True

# LOGIN LOGOUT URL SET
# LOGIN_REDIRECT_URL = 'product:home'
# LOGOUT_REDIRECT_URL = 'accounts:login'
# LOGIN_URL = 'accounts:login'
# LOGOUT_URL = 'accounts:logout'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
