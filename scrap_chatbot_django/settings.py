from pathlib import Path
import os

"""
user: admin
pass: admin
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "wz24!p!5i!=i2-ygz!=n#t&qzl=@tbw339$in+4rjd=t5@p5g!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    ".herokuapp.com",
    "127.0.0.1",
    "*"
]

# Application definition

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # install app
    'rest_framework',
    'corsheaders',

    # custom app
    "scrap.apps.ScrapConfig",
    "auth_acc.apps.AuthAccConfig",
    'api_chat_video.apps.ApiChatVideoConfig'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    'corsheaders.middleware.CorsMiddleware',

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
# ]
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "scrap_chatbot_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates/"],
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

WSGI_APPLICATION = "scrap_chatbot_django.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
""" using sql server
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'WebDjangoLearn',
        'HOST': 'databasehienco.cidw3wkwqevk.us-east-1.rds.amazonaws.com',
        'USER': 'hien363',
        'PASSWORD': 'hien0362363616',
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
    }
}
"""
# using postgresql
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "learnwebdjango",
        "USER": "sa",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# important
STATIC_URL = "/static/"
# important
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/static"),
    "/var/www/static/",
]

LOGIN_REDIRECT_URL = "/login/profile/"
