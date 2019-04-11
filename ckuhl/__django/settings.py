from pathlib import Path


BASE_DIR: Path = Path(__file__).parent.parent.absolute()

SECRET_KEY = 'record-lowest-bisect-regent-songbird-freedmen-hoyden-salivary'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# Application definition ===================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    '_commons.apps.CommonsConfig',

    'core.apps.CoreConfig',
    'blog.apps.BlogConfig',
    'portfolio.apps.PortfolioConfig',
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

ROOT_URLCONF = '__django.urls'

# Templating ===============================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                '_commons.context_processors.do_not_track',
            ],
            'libraries': {
                'html_tags': '_commons.templatetags.html_tags',
            },
        },
    },
]

WSGI_APPLICATION = '__django.wsgi.application'

# Database =================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR.parent / 'db.sqlite3'),
    },
}

# Password validation ======================================================
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

# Internationalization =====================================================
LANGUAGE_CODE = 'en-ca'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static resources =========================================================
# Stores static files to serve
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR.parent / 'static',
]

# Media resources ==========================================================
# Stores user uploaded files
MEDIA_URL = '/media/'

MEDIAFILES_DIRS = [
    BASE_DIR.parent / 'media',
]

# Local resources ==========================================================
# Stores local files that shouldn't be served

RESOURCEFILES_DIR: Path = BASE_DIR.parent / 'resources'

# Logging ==================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(name)s:%(levelname)s: %(message)s',
        },
        'complex': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
