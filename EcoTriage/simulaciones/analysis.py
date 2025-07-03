import pandas as pd
from django.db.models import Avg, Count, Sum
from .models import SimulacionAmbiental

def procesar_simulaciones(datos_queryset):
    """
    Procesa las simulaciones ambientales usando Pandas para generar análisis
    """
    if not datos_queryset.exists():
        return {
            'error': 'No hay datos suficientes para el análisis',
            'total_simulaciones': 0
        }
    
    # Convertir QuerySet a DataFrame de Pandas
    df = pd.DataFrame(list(datos_queryset.values()))
    
    # Análisis básico
    total_simulaciones = len(df)
    edad_promedio = df['edad'].mean()
    
    # Análisis de transporte
    km_promedio_dia = df['km_por_dia'].mean()
    transporte_mas_usado = df['medio_transporte'].mode()[0] if not df['medio_transporte'].mode().empty else 'N/A'
    
    # Análisis de alimentación
    carne_promedio_semana = df['carne_por_semana'].mean()
    vegetales_promedio_semana = df['vegetales_por_semana'].mean()
    
    # Análisis de energía
    horas_luz_promedio = df['horas_luz_dia'].mean()
    
    # Análisis de residuos
    porcentaje_separa_residuos = (df['separa_residuos'].sum() / len(df)) * 100
    
    # Análisis por ciudad
    ciudades_participantes = df['ciudad'].nunique()
    ciudad_mas_participativa = df['ciudad'].mode()[0] if not df['ciudad'].mode().empty else 'N/A'
    
    # Cálculo de huella de carbono aproximada (kg CO2 por día)
    def calcular_huella_carbono(row):
        huella = 0
        
        # Transporte (kg CO2 por km según medio)
        factores_transporte = {
            'Bus': 0.089,
            'Auto': 0.21,
            'Moto': 0.113,
            'Bicicleta': 0,
            'Caminando': 0,
            'Taxi': 0.25
        }
        factor = factores_transporte.get(row['medio_transporte'], 0.15)  # default promedio
        huella += row['km_por_dia'] * factor
        
        # Alimentación (kg CO2 por porción por semana / 7 días)
        huella += (row['carne_por_semana'] * 6.61) / 7  # carne roja alta huella
        huella += (row['vegetales_por_semana'] * 0.43) / 7  # vegetales baja huella
        
        # Energía (kg CO2 por kWh - estimando 0.1 kWh por hora de luz)
        huella += row['horas_luz_dia'] * 0.1 * 0.45  # factor eléctrico Perú
        
        # Bonus por separación de residuos (reducción 10%)
        if row['separa_residuos']:
            huella *= 0.9
            
        return round(huella, 2)
    
    df['huella_carbono_dia'] = df.apply(calcular_huella_carbono, axis=1)
    huella_promedio = df['huella_carbono_dia'].mean()
    
    # Clasificación de usuarios por huella
    def clasificar_usuario(huella):
        if huella < 5:
            return 'Eco-Héroe'
        elif huella < 10:
            return 'Consciente'
        elif huella < 15:
            return 'En Camino'
        else:
            return 'Necesita Mejorar'
    
    df['clasificacion'] = df['huella_carbono_dia'].apply(clasificar_usuario)
    clasificaciones = df['clasificacion'].value_counts().to_dict()
    
    # Recomendaciones personalizadas
    recomendaciones = []
    
    if km_promedio_dia > 15:
        recomendaciones.append("🚌 Considera usar más transporte público o bicicleta")
    
    if carne_promedio_semana > 5:
        recomendaciones.append("🥬 Intenta reducir el consumo de carne a 3-4 veces por semana")
    
    if horas_luz_promedio > 6:
        recomendaciones.append("💡 Usa focos LED y aprovecha más la luz natural")
    
    if porcentaje_separa_residuos < 70:
        recomendaciones.append("♻️ Implementa la separación de residuos en tu hogar")
    
    # Comparación con estándares
    huella_objetivo_peru = 8.5  # kg CO2 per cápita objetivo para Perú
    diferencia_objetivo = huella_promedio - huella_objetivo_peru
    
    return {
        'total_simulaciones': total_simulaciones,
        'edad_promedio': round(edad_promedio, 1),
        'km_promedio_dia': round(km_promedio_dia, 1),
        'transporte_mas_usado': transporte_mas_usado,
        'carne_promedio_semana': round(carne_promedio_semana, 1),
        'vegetales_promedio_semana': round(vegetales_promedio_semana, 1),
        'horas_luz_promedio': round(horas_luz_promedio, 1),
        'porcentaje_separa_residuos': round(porcentaje_separa_residuos, 1),
        'ciudades_participantes': ciudades_participantes,
        'ciudad_mas_participativa': ciudad_mas_participativa,
        'huella_promedio': round(huella_promedio, 2),
        'clasificaciones': clasificaciones,
        'recomendaciones': recomendaciones,
        'diferencia_objetivo': round(diferencia_objetivo, 2),
        'huella_objetivo': huella_objetivo_peru,
        'datos_detallados': df.to_dict('records')[:10]  # Últimos 10 registros para mostrar
    }

def generar_reporte_individual(simulacion_id):
    """
    Genera un reporte individual para una simulación específica
    """
    try:
        simulacion = SimulacionAmbiental.objects.get(id=simulacion_id)
        
        # Calcular huella individual
        huella = 0
        factores_transporte = {
            'Bus': 0.089, 'Auto': 0.21, 'Moto': 0.113,
            'Bicicleta': 0, 'Caminando': 0, 'Taxi': 0.25
        }
        
        factor = factores_transporte.get(simulacion.medio_transporte, 0.15)
        huella += simulacion.km_por_dia * factor
        huella += (simulacion.carne_por_semana * 6.61) / 7
        huella += (simulacion.vegetales_por_semana * 0.43) / 7
        huella += simulacion.horas_luz_dia * 0.1 * 0.45
        
        if simulacion.separa_residuos:
            huella *= 0.9
            
        # Clasificación
        if huella < 5:
            clasificacion = 'Eco-Héroe'
            mensaje = '¡Excelente! Tienes hábitos muy sostenibles.'
        elif huella < 10:
            clasificacion = 'Consciente'
            mensaje = 'Buen trabajo, sigues el camino correcto hacia la sostenibilidad.'
        elif huella < 15:
            clasificacion = 'En Camino'
            mensaje = 'Vas bien, pero puedes mejorar algunos hábitos.'
        else:
            clasificacion = 'Necesita Mejorar'
            mensaje = 'Es momento de hacer cambios significativos por el planeta.'
        
        return {
            'simulacion': simulacion,
            'huella_carbono': round(huella, 2),
            'clasificacion': clasificacion,
            'mensaje': mensaje,
            'huella_objetivo': 8.5
        }
        
    except SimulacionAmbiental.DoesNotExist:
        return {'error': 'Simulación no encontrada'}