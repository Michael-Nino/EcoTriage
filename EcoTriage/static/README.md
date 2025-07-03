# Carpeta: static

## ¿Qué es la carpeta static?
Esta carpeta almacena todos los archivos estáticos del proyecto, es decir, archivos que no cambian en el servidor y que se envían tal cual al navegador del usuario.

## ¿Qué tipo de archivos contiene?
- Hojas de estilo CSS (para el diseño visual)
- Imágenes (PNG, JPG, SVG, etc.)
- Archivos JavaScript (JS) para interactividad
- Fuentes, íconos, videos, etc.

## ¿Cómo funciona en Django?
- Cuando usas `{% load static %}` en una plantilla, puedes referenciar archivos de esta carpeta con `{% static 'ruta/archivo' %}`.
- Django recopila todos los archivos estáticos de cada app y los sirve desde aquí en desarrollo.
- En producción, normalmente se configuran servidores web (como Nginx) para servir estos archivos de manera eficiente.

## Organización recomendada
```
static/
    css/
        style.css      # Estilos personalizados del sitio
    img/
        logo.png       # Imágenes usadas en la web
    js/
        scripts.js     # Scripts JavaScript
```

## Ventajas
- Permite separar el código de presentación (CSS, JS) del backend.
- Facilita la reutilización de recursos visuales y scripts en todo el proyecto.

## Mejoras recientes (julio 2025)
- Mejor contraste y accesibilidad en botones principales (`btn-eco-primary`).
- Filas alternas y efecto hover más notorio en tablas para mejor lectura.
- Iconos de acción más grandes y accesibles.
- Mejoras visuales y de usabilidad en pantallas pequeñas.
- Sombra sutil en tarjetas de recomendación.
- Mejora el rendimiento al permitir el cacheo de archivos estáticos en el navegador del usuario.

## Notas
- No almacenes archivos sensibles aquí, ya que son públicos.
- Puedes tener archivos estáticos globales y específicos por app.
