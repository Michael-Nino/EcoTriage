
# Definición de las rutas (URLs) de la app 'simulaciones'
from django.urls import path
from . import views

# Lista de rutas disponibles en la app
urlpatterns = [
    # Ruta principal: formulario de registro de simulación
    path('', views.registrar_simulacion, name='registro'),
    # Resultados generales de todas las simulaciones
    path('resultados/', views.ver_resultados, name='resultados'),
    # Dashboard con análisis y estadísticas
    path('dashboard/', views.dashboard, name='dashboard'),
    # Reporte individual de una simulación
    path('reporte/<int:simulacion_id>/', views.reporte_individual, name='reporte_individual'),
    # API para obtener estadísticas en formato JSON
    path('api/estadisticas/', views.api_estadisticas, name='api_estadisticas'),
    # Eliminar una simulación específica
    path('eliminar/<int:simulacion_id>/', views.eliminar_simulacion, name='eliminar_simulacion'),
]