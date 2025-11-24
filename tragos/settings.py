# settings.py

from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Configuración básica
# -------------------------
SECRET_KEY = 'tu_clave_secreta_aqui'
DEBUG = True
ALLOWED_HOSTS = ['*']   # <--- CAMBIO NECESARIO

# -------------------------
# Aplicaciones instaladas
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # tu app de tragos
]

# -------------------------
# Middleware
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tragos.urls'

# -------------------------
# Templates
# -------------------------
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
            ],
        },
    },
]

WSGI_APPLICATION = 'tragos.wsgi.application'

# -------------------------
# Base de datos (SQLite por defecto)
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# Contraseñas
# -------------------------
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

# -------------------------
# Internacionalización
# -------------------------
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# -------------------------
# Archivos estáticos
# -------------------------
#STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR / 'staticfiles']


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -------------------------
# Archivos media (imágenes subidas)
# -------------------------
MEDIA_URL = '/media/'              # URL que se usará en templates
MEDIA_ROOT = BASE_DIR / 'media'    # Carpeta física en tu proyecto

# -------------------------
# Otros
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
