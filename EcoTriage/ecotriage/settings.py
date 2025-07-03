
# Importa módulos necesarios para la configuración de Django
import os
from pathlib import Path
from dotenv import load_dotenv

# Carga variables de entorno desde un archivo .env (útil para mantener claves y configuraciones sensibles fuera del código)
load_dotenv()


# Define la ruta base del proyecto (directorio raíz)
BASE_DIR = Path(__file__).resolve().parent.parent


# Clave secreta para la seguridad de Django (debe cambiarse en producción)
SECRET_KEY = 'django-insecure-clave-temporal'

# Activa el modo debug (muestra errores detallados, solo para desarrollo)
DEBUG = True

# Lista de hosts permitidos para acceder a la aplicación (usar ['*'] solo en desarrollo)
ALLOWED_HOSTS = ['*']


# Definición de las aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    # Apps principales de Django para administración, autenticación, sesiones, etc.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # App personalizada para simulaciones ambientales
    'simulaciones',
]


# Lista de middlewares que procesan las peticiones/respuestas HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Seguridad básica
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',  # Funcionalidades comunes
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware',  # Mensajes entre vistas
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protección contra clickjacking
]


# Archivo principal de rutas (urls) del proyecto
ROOT_URLCONF = 'ecotriage.urls'


# Configuración del sistema de plantillas de Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de plantillas
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta donde se buscan los templates personalizados
        'APP_DIRS': True,  # Busca templates dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Añade variables de depuración
                'django.template.context_processors.request',  # Añade el objeto request
                'django.contrib.auth.context_processors.auth',  # Añade usuario autenticado
                'django.contrib.messages.context_processors.messages',  # Añade mensajes
            ],
        },
    },
]


# Configuración para el servidor WSGI (despliegue en producción)
WSGI_APPLICATION = 'ecotriage.wsgi.application'


# Configuración de la base de datos (MySQL en este caso)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Motor de base de datos
        'NAME': 'ecotriage_db',               # Nombre de la base de datos
        'USER': 'eco_user',                   # Usuario de la base de datos
        'PASSWORD': 'eco_pass',               # Contraseña del usuario
        'HOST': 'localhost',                  # Host de la base de datos
        'PORT': '3306',                       # Puerto de conexión
    }
}

# Configuración de internacionalización y zona horaria
LANGUAGE_CODE = 'es-pe'         # Idioma por defecto
TIME_ZONE = 'America/Lima'      # Zona horaria local

USE_I18N = True                 # Habilita la traducción de textos
USE_TZ = True                   # Usa zonas horarias con soporte UTC

# Configuración de archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Tipo de campo automático por defecto para modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'