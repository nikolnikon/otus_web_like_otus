import os
from configurations import Configuration, values
from django.urls import reverse_lazy


class Base(Configuration):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'registration',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'courses.apps.CoursesConfig',
        'users.apps.UsersConfig',
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

    ROOT_URLCONF = 'like_otus.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates'],
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

    WSGI_APPLICATION = 'like_otus.wsgi.application'

    DATABASES = values.DatabaseURLValue('postgres://postgres:12345678@localhost/like_otus')

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

    AUTH_USER_MODEL = 'users.User'

    LANGUAGE_CODE = 'ru-ru'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    MEDIA_URL = '/media/'

    SIMPLE_BACKEND_REDIRECT_URL = reverse_lazy('courses:list')

    LOGIN_REDIRECT_URL = reverse_lazy('courses:list')


class Dev(Base):
    DEBUG = True
    SECRET_KEY = 'dev'


class Prod(Base):
    DEBUG = False
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = ['localhost']
