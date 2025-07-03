
# Archivo principal de rutas del proyecto
# Aquí se definen las URLs globales y se incluyen las de cada app
from django.contrib import admin
from django.urls import path, include

# Lista de rutas principales del proyecto
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    # Incluye las rutas definidas en la app 'simulaciones'
    path('', include('simulaciones.urls')),
]
