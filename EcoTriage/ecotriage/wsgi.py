os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecotriage.settings')

# Configuración para el servidor WSGI (Web Server Gateway Interface)
# Permite que Django funcione con servidores web tradicionales (como Gunicorn, uWSGI, Apache mod_wsgi)
import os
from django.core.wsgi import get_wsgi_application

# Establece la variable de entorno para que Django sepa qué archivo de configuración usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecotriage.settings')

# Obtiene la aplicación WSGI para ser utilizada por servidores compatibles
application = get_wsgi_application()