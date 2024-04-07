# Importar las bibliotecas necesarias
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import os
import json

# Este es el nuevo JSON de ejemplo que representa los datos completos de la factura
datos_json = """
{
  "invoice_id": "123456",
  "issue_date": "2024-04-01",
  "due_date": "2024-04-15",
  "issuer": {
    "name": "Company Name",
    "address": "Company Address",
    "phone": "123456789",
    "email": "contact@company.com",
    "tax_id": "XYZ123456"
  },
  "recipient": {
    "name": "mery mery",
    "address": "Customer Address",
    "phone": "987654321",
    "email": "customer@example.com",
    "tax_id": "ABC987654"
  },
  "items": [
    {
      "description": "Product or Service 1",
      "quantity": 2,
      "unit_price": 100.00,
      "total": 200.00
    },
    {
      "description": "Product or Service 2",
      "quantity": 1,
      "unit_price": 50.00,
      "total": 50.00
    }
  ],
  "subtotal": 250.00,
  "taxes": [
    {
      "description": "VAT",
      "percentage": 16,
      "amount": 40.00
    }
  ],
  "total": 290.00,
  "payment_method": "Credit Card"
  "currency": "EUR"
  }
"""

# Parsear el JSON para convertirlo en una estructura de datos de Python
datos_factura = json.loads(datos_json)


# Configurar Jinja2 para cargar la plantilla desde el directorio actual
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

logo_path = 'file://' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'logo.png')

# Usar Jinja2 para rellenar la plantilla con los datos. `render` reemplaza las variables en la plantilla con los valores dados
html_output = template.render(
    invoice_id=datos_factura['invoice_id'],
    issue_date=datos_factura['issue_date'],
    due_date=datos_factura['due_date'],
    issuer=datos_factura['issuer'],
    recipient=datos_factura['recipient'],
    items=datos_factura['items'],
    subtotal=datos_factura['subtotal'],
    taxes=datos_factura['taxes'],
    total=datos_factura['total'],
    payment_method=datos_factura['payment_method'],
    logo_path=logo_path
)

css = CSS(filename='template.css')
# Generar un PDF a partir del HTML renderizado con WeasyPrint. `write_pdf` toma el HTML y lo convierte en un documento PDF
HTML(string=html_output).write_pdf('factura_generada.pdf', stylesheets=[css])



print(html_output)
# Indicación de finalización
print("La factura ha sido generada con éxito y está guardada como 'factura_generada.pdf'")
