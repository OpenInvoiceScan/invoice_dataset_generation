from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Datos de ejemplo basados en tu estructura JSON
invoice_data = {
    "invoice_id": "123456",
    "issue_date": "2024-04-01",
    "due_date": "2024-04-15",
    "issuer": {"name": "Company Name"},
    "recipient": {"name": "Customer Name"},
    "items": [
        {"description": "Product or Service 1", "quantity": 2, "unit_price": 100.00, "total": 200.00},
        {"description": "Product or Service 2", "quantity": 1, "unit_price": 50.00, "total": 50.00},
    ],
    "subtotal": 250.00,
    "taxes": [{"description": "VAT", "percentage": 16, "amount": 40.00}],
    "total": 290.00,
    "payment_method": "Credit Card"
}

def create_invoice(pdf_filename, invoice_data):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    
    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "Invoice")

    # Información básica de la factura
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 108, f"Invoice ID: {invoice_data['invoice_id']}")
    c.drawString(72, height - 124, f"Issue Date: {invoice_data['issue_date']}")
    c.drawString(72, height - 140, f"Due Date: {invoice_data['due_date']}")

    # Información del emisor y receptor
    c.drawString(72, height - 176, f"Issuer: {invoice_data['issuer']['name']}")
    c.drawString(72, height - 192, f"Recipient: {invoice_data['recipient']['name']}")

    # Detalle de los items
    start_y = height - 228
    for item in invoice_data['items']:
        c.drawString(72, start_y, f"{item['description']} - Qty: {item['quantity']} - Unit Price: {item['unit_price']} - Total: {item['total']}")
        start_y -= 16

    # Totales
    c.drawString(72, start_y - 32, f"Subtotal: {invoice_data['subtotal']}")
    c.drawString(72, start_y - 48, f"VAT: {invoice_data['taxes'][0]['amount']}")
    c.drawString(72, start_y - 64, f"Total: {invoice_data['total']}")

    # Método de pago
    c.drawString(72, start_y - 100, f"Payment Method: {invoice_data['payment_method']}")

    c.save()

# Crear el PDF
create_invoice("invoice_example.pdf", invoice_data)
