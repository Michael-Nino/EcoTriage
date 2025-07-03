
# Vistas principales de la app 'simulaciones'
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import SimulacionForm
from .models import SimulacionAmbiental
from .analysis import procesar_simulaciones, generar_reporte_individual

def registrar_simulacion(request):
    """
    Vista para registrar una nueva simulación ambiental.
    Si la petición es POST, procesa el formulario y guarda la simulación.
    Si es GET, muestra el formulario vacío.
    También muestra el total de simulaciones registradas.
    """
    if request.method == 'POST':
        form = SimulacionForm(request.POST)
        if form.is_valid():
            simulacion = form.save()
            messages.success(
                request, 
                f'¡Simulación registrada exitosamente! Tu huella de carbono ha sido calculada.'
            )
            return redirect('reporte_individual', simulacion_id=simulacion.id)
        else:
            messages.error(
                request, 
                'Por favor corrige los errores en el formulario.'
            )
    else:
        form = SimulacionForm()
    # Estadísticas rápidas para mostrar en el formulario
    total_simulaciones = SimulacionAmbiental.objects.count()
    context = {
        'form': form,
        'total_simulaciones': total_simulaciones,
        'title': 'EcoTriage - Simula tu Impacto Ambiental'
    }
    return render(request, 'registro.html', context)

def ver_resultados(request):
    """
    Vista para mostrar resultados generales de todas las simulaciones.
    Realiza análisis estadístico y muestra los resultados paginados.
    """
    datos = SimulacionAmbiental.objects.all().order_by('-fecha')
    analisis = procesar_simulaciones(datos)
    # Paginación para datos detallados
    paginator = Paginator(datos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'analisis': analisis,
        'page_obj': page_obj,
        'title': 'Resultados Generales - EcoTriage'
    }
    return render(request, 'resultados.html', context)

def reporte_individual(request, simulacion_id):
    """
    Vista para mostrar el reporte individual de una simulación
    """
    reporte = generar_reporte_individual(simulacion_id)
    
    if 'error' in reporte:
        messages.error(request, reporte['error'])
        return redirect('registro')
    
    context = {
        'reporte': reporte,
        'title': f'Tu Reporte Ambiental - EcoTriage'
    }
    
    return render(request, 'reporte_individual.html', context)

def dashboard(request):
    """
    Vista del dashboard principal con estadísticas
    """
    total_simulaciones = SimulacionAmbiental.objects.count()
    
    if total_simulaciones == 0:
        context = {
            'sin_datos': True,
            'title': 'Dashboard - EcoTriage'
        }
        return render(request, 'dashboard.html', context)
    
    datos = SimulacionAmbiental.objects.all()
    analisis = procesar_simulaciones(datos)
    
    # Simulaciones recientes
    simulaciones_recientes = SimulacionAmbiental.objects.order_by('-fecha')[:5]
    
    context = {
        'analisis': analisis,
        'simulaciones_recientes': simulaciones_recientes,
        'title': 'Dashboard - EcoTriage'
    }
    
    return render(request, 'dashboard.html', context)

def api_estadisticas(request):
    """
    API endpoint para obtener estadísticas en formato JSON
    """
    datos = SimulacionAmbiental.objects.all()
    analisis = procesar_simulaciones(datos)
    
    # Remover datos detallados para API
    if 'datos_detallados' in analisis:
        del analisis['datos_detallados']
    
    return JsonResponse(analisis)

def eliminar_simulacion(request, simulacion_id):
    """
    Vista para eliminar una simulación (solo para demostración)
    """
    if request.method == 'POST':
        simulacion = get_object_or_404(SimulacionAmbiental, id=simulacion_id)
        simulacion.delete()
        messages.success(request, 'Simulación eliminada correctamente.')
        return redirect('resultados')
    
    return redirect('resultados')