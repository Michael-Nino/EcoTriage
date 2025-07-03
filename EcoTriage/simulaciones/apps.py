
# Configuración de la app 'simulaciones' para Django
from django.apps import AppConfig

class SimulacionesConfig(AppConfig):
    # Define el tipo de campo automático por defecto para los modelos de esta app
    default_auto_field = 'django.db.models.BigAutoField'
    # Nombre de la app (debe coincidir con el nombre de la carpeta)
    name = 'simulaciones'