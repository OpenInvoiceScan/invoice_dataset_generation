# Importar las bibliotecas necesarias
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import json

# Este es el JSON de ejemplo que representa los datos de los ítems de la factura
datos_json = """
[
    {"producto": "Producto A", "cantidad": 2, "precio": 100},
    {"producto": "Producto B", "cantidad": 1, "precio": 200}
]
"""

# Parsear el JSON para convertirlo en una estructura de datos de Python
datos_factura = json.loads(datos_json)

# Configurar Jinja2 para cargar la plantilla desde el directorio actual
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Usar Jinja2 para rellenar la plantilla con los datos. `render` reemplaza las variables en la plantilla con los valores dados
html_output = template.render(items=datos_factura)

# Generar un PDF a partir del HTML renderizado con WeasyPrint. `write_pdf` toma el HTML y lo convierte en un documento PDF
HTML(string=html_output).write_pdf('factura_generada.pdf')

# Indicación de finalización
print("La factura ha sido generada con éxito y está guardada como 'factura_generada.pdf'")
