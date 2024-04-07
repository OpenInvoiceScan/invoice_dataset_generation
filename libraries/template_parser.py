
import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

'''

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
'''


def parse_template(json, template_dir , output_pdf_path, output_pdf_name):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('template.html')

    abs_template_dir = os.path.abspath(template_dir)
    
    # Construye la ruta hacia el logo, asumiendo que está en un subdirectorio 'img'
    logo_path = 'file://' + os.path.join(abs_template_dir, 'img', 'logo.png')
    print(logo_path)
    

    # Usar Jinja2 para rellenar la plantilla con los datos. `render` reemplaza las variables en la plantilla con los valores dados
    html_output = template.render(
        invoice_id=json['invoice_id'],
        issue_date=json['issue_date'],
        due_date=json['due_date'],
        issuer=json['issuer'],
        recipient=json['recipient'],
        items=json['items'],
        subtotal=json['subtotal'],
        taxes=json['taxes'],
        total=json['total'],
        payment_method=json['payment_method'],
        logo_path=logo_path
    )

    css = CSS(filename=f'{template_dir}/template.css')
    # Generar un PDF a partir del HTML renderizado con WeasyPrint. `write_pdf` toma el HTML y lo convierte en un documento PDF
    HTML(string=html_output).write_pdf( output_pdf_path + output_pdf_name, stylesheets=[css])
    return 'factura_generada.pdf'
