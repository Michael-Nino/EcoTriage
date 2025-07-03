# Carpeta: templates

## ¿Qué es la carpeta templates?
Esta carpeta es fundamental en cualquier proyecto Django, ya que aquí se almacenan todas las plantillas HTML que definen la estructura visual y el contenido dinámico de las páginas web que verá el usuario.

## ¿Cómo funciona?
- Django utiliza el sistema de plantillas para separar la lógica del backend (Python) de la presentación (HTML).
- Cuando una vista de Django llama a `render(request, 'archivo.html', contexto)`, busca el archivo HTML dentro de la carpeta `templates`.
- Las plantillas pueden contener variables y etiquetas especiales de Django (como `{% block %}`, `{% for %}`, `{% if %}`, y `{{ variable }}`) que permiten mostrar datos dinámicos y reutilizar fragmentos de código.

## Organización recomendada
- Puedes tener plantillas globales (como `base.html`) y plantillas específicas para cada app dentro de subcarpetas.
- Ejemplo:
  ```
  templates/
      base.html                # Plantilla base para todo el sitio
      dashboard.html           # Página principal del usuario
      registro.html            # Formulario de registro
      resultados.html          # Resultados y estadísticas
      reporte_individual.html  # Reporte personalizado de cada simulación (nuevo)
      simulaciones/
          formulario.html      # Plantilla específica de la app simulaciones
          reporte.html         # Otra plantilla específica
  ```

## Ventajas
- Permite reutilizar código HTML (por ejemplo, menús, cabeceras, pies de página) usando herencia de plantillas.
- Facilita la colaboración entre desarrolladores backend y frontend.
- Hace posible el diseño de sitios web dinámicos y personalizados para cada usuario.

## Notas

- `reporte_individual.html`: Muestra el reporte personalizado de cada simulación, incluyendo huella de carbono, clasificación y recomendaciones. Se enlaza desde la tabla de resultados generales.
- Django busca automáticamente en esta carpeta si está bien configurada en `settings.py`.
- Puedes usar la etiqueta `{% extends 'base.html' %}` para heredar la estructura de una plantilla base.
- Las plantillas pueden incluir archivos estáticos (CSS, JS, imágenes) usando `{% load static %}` y `{% static 'ruta/archivo' %}`.
