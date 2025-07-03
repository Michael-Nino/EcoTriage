
# Registro del modelo SimulacionAmbiental en el panel de administración de Django
from django.contrib import admin
from .models import SimulacionAmbiental

# Permite gestionar las simulaciones ambientales desde el admin
admin.site.register(SimulacionAmbiental)
