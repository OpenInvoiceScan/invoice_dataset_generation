
import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import pdfkit
import libraries.html_img_embedder as html_img_embedder
import libraries.css_font_embedder as css_font_embedder

import asyncio
from pyppeteer import launch


async def html_to_pdf(html_content, css_path, output_path):
    # Lanzar un navegador sin cabeza
    browser = await launch(headless=True)
    
    # Abrir una nueva página
    page = await browser.newPage()
    
    await page.setViewport({'width': 1280, 'height': 926})

    # Agregar contenido HTML a la página
    await page.setContent(html_content)
    
    # Incluir el CSS si está disponible
    if css_path and os.path.exists(css_path):
        with open(css_path, 'r') as css_file:
            css_content = css_file.read()
            css_content = css_font_embedder.embed_fonts_in_css(css_content, os.path.dirname(css_path))
        await page.addStyleTag(content=css_content)
    
    await page.addStyleTag({ 'content': 'body, html { margin: 0; padding: 0; border: 0 }' })

    # Wait until css_content is loaded
    await page.waitForFunction('document.fonts.ready')
    
    
    # Guardar la página en formato PDF
    
    await page.pdf({
        'path': output_path,
        'preferCSSPageSize': True,
        'printBackground': True,
        'margin': {
        'top': '0px',
        'right': '0px',
        'bottom': '0px',
        'left': '0px',
        }
    })    
    
    # Cerrar el navegador
    await browser.close()

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
    #env = Environment(loader=FileSystemLoader(template_dir))
    #template = env.get_template('template.html')
    
    template = os.path.join(template_dir, 'template.html')
    #Read the template file
    with open(template, 'r') as file:
        template_content = file.read()
    
    # Create a Jinja2 template object
    template_content = html_img_embedder.embed_images_in_html(template_content, template_dir)
    
    template = Environment(loader=FileSystemLoader(template_dir)).from_string(template_content)
    
    

    abs_template_dir = os.path.abspath(template_dir)
    
    # Construye la ruta hacia el logo, asumiendo que está en un subdirectorio 'img'
    logo_path = 'file://' + os.path.join(abs_template_dir, 'img', 'logo.png')
    

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

    
    # Ruta del archivo HTML y del PDF de salida
    output_pdf = os.path.join(output_pdf_path, output_pdf_name)
    css_path = os.path.join(template_dir, 'template.css')

    # Ejecutar la conversión a PDF usando asyncio con Puppeteer
    asyncio.get_event_loop().run_until_complete(html_to_pdf(html_output, css_path, output_pdf))

    return output_pdf
