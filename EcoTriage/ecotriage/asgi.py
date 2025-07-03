os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecotriage.settings')

# Configuración para el servidor ASGI (Asynchronous Server Gateway Interface)
# Permite que Django funcione con servidores asíncronos y aplicaciones en tiempo real.
import os
from django.core.asgi import get_asgi_application

# Establece la variable de entorno para que Django sepa qué archivo de configuración usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecotriage.settings')

# Obtiene la aplicación ASGI para ser utilizada por servidores compatibles (como Daphne o Uvicorn)
application = get_asgi_application()
