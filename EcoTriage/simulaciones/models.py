
# Definición de los modelos de la app 'simulaciones'
from django.db import models

class SimulacionAmbiental(models.Model):
    # Fecha y hora en que se registró la simulación (se asigna automáticamente)
    fecha = models.DateTimeField(auto_now_add=True)

    # Datos personales
    edad = models.PositiveIntegerField()  # Edad del usuario
    ciudad = models.CharField(max_length=100)  # Ciudad de residencia

    # Datos de transporte
    km_por_dia = models.FloatField()  # Kilómetros recorridos por día
    medio_transporte = models.CharField(max_length=50)  # Medio de transporte principal

    # Datos de alimentación
    carne_por_semana = models.PositiveIntegerField()  # Veces que consume carne por semana
    vegetales_por_semana = models.PositiveIntegerField()  # Veces que consume vegetales por semana

    # Datos de energía y residuos
    horas_luz_dia = models.FloatField()  # Horas de luz artificial por día
    separa_residuos = models.BooleanField()  # Si separa residuos o no

    def __str__(self):
        # Representación legible de la simulación (útil en el admin)
        return f"Simulación en {self.ciudad} el {self.fecha.date()}"