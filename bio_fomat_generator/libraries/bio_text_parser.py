import json
import textwrap

'''
Tags for the NER model
labels = [
    "O",  # Para tokens que no son parte de ninguna entidad nombrada
    "B-invoice_id", "I-invoice_id",
    "B-issue_date", "I-issue_date",
    "B-due_date", "I-due_date",
    "B-issuer_name", "I-issuer_name",
    "B-issuer_address", "I-issuer_address",
    "B-issuer_phone",
    "B-issuer_email",
    "B-issuer_tax_id",
    "B-recipient_name", "I-recipient_name",
    "B-recipient_address", "I-recipient_address",
    "B-recipient_phone",
    "B-recipient_email",
    "B-recipient_tax_id",
    "B-item_description", "I-item_description",
    "B-item_quantity",
    "B-item_unit_price",
    "B-item_total",
    "B-subtotal",
    "B-tax_description", "I-tax_description",
    "B-tax_percentage",
    "B-tax_amount",
    "B-total",
    "B-payment_method",
    "UNK"
]
'''

'''
Example of generated data:
{
  "invoice_id": 396662,
  "issue_date": "2024-04-04",
  "due_date": "2024-04-13",
  "issuer": {
    "name": "Joseph, Webster and Smith",
    "address": "7179 Porter Shoal Suite 414\nAllenshire, MN 84280",
    "phone": "001-384-278-0921x027",
    "email": "wilsonjessica@brown-everett.org",
    "tax_id": "Njn208dIN762"
  },
  "recipient": {
    "name": "Nicholas Braun",
    "address": "USS Mayer\nFPO AE 68397",
    "phone": "(835)615-1959",
    "email": "jimmy97@gmail.com",
    "tax_id": "hLT932idX354"
  },
  "items": [
    {
      "description": "orchestrate bricks-and-clicks paradigms",
      "quantity": 8,
      "unit_price": 44.86,
      "total": 358.88
    },
    {
      "description": "whiteboard real-time e-markets",
      "quantity": 6,
      "unit_price": 53.6,
      "total": 321.6
    },
    {
      "description": "synergize bleeding-edge convergence",
      "quantity": 4,
      "unit_price": 82.28,
      "total": 329.12
    },
    {
      "description": "engage best-of-breed e-services",
      "quantity": 7,
      "unit_price": 35.11,
      "total": 245.77
    },
    {
      "description": "brand magnetic e-commerce",
      "quantity": 3,
      "unit_price": 86.26,
      "total": 258.78
    }
  ],
  "subtotal": 1514.15,
  "taxes": [
    {
      "description": "VAT",
      "percentage": 16,
      "amount": 242.26
    }
  ],
  "total": 1756.41,
  "payment_method": "Bank Transfer",
  "currency": "EUR"
}
'''


def issue_date_to_bio(data):
    json_data = json.loads(data)

    # Extract the issue date
    issue_date = json_data['issue_date']

    # Generate additional text to be used as context
    text = textwrap.dedent(f"""
              Fecha -> O
              de -> O
              emisión -> O
              : -> O
              {issue_date} -> B-issue_date
              """).strip()
    
    return text

def due_date_to_bio(data):
    json_data = json.loads(data)

    # Extract the due date
    due_date = json_data['due_date']

    # Generate additional text to be used as context
    text = textwrap.dedent(f"""
          Fecha -> O
          de -> O
          vencimiento -> O
          : -> O
          {due_date} -> B-due_date
          """).strip()
    
    
    return text

def invoice_id_to_bio(data):
    json_data = json.loads(data)

    # Extract the invoice id
    invoice_id = json_data['invoice_id']

    # Generate additional text to be used as context
    text = textwrap.dedent(f"""
          Factura -> O
          : -> O
          #{invoice_id} -> B-invoice_id
          """).strip()
    
    return text

def issuer_name_to_bio(data):
    json_data = json.loads(data)

    # Extract the issuer name
    issuer_name = json_data['issuer']['name']
    
    issuer_name = issuer_name.split()
    
    text = textwrap.dedent(f"""
          Datos -> O
          del -> O
          Emisor -> O
          : -> O
          """)
     
    for i, name in enumerate(issuer_name):
        if i == 0:
            text += f"{name} -> B-issuer_name\n"
        else:
            text += f"{name} -> I-issuer_name\n"
    
    return textwrap.dedent(text).strip()
  
def issuer_address_to_bio(data):
    json_data = json.loads(data)

    # Extract the issuer address
    issuer_address = json_data['issuer']['address']
    
    issuer_address = issuer_address.split()
    text = ""
     
    for i, address in enumerate(issuer_address):
        if i == 0:
            text += f"{address} -> B-issuer_address\n"
        else:
            text += f"{address} -> I-issuer_address\n"
    
    return textwrap.dedent(text).strip()

def issuer_phone_to_bio(data):
    json_data = json.loads(data)

    # Extract the issuer phone
    issuer_phone = json_data['issuer']['phone']

    return f'{issuer_phone} -> B-issuer_phone'

def issuer_email_to_bio(data):
    json_data = json.loads(data)

    # Extract the issuer email
    issuer_email = json_data['issuer']['email']

    return f'{issuer_email} -> B-issuer_email'

def issuer_tax_id_to_bio(data):
    json_data = json.loads(data)

    # Extract the issuer tax id
    issuer_tax_id = json_data['issuer']['tax_id']

    return f'{issuer_tax_id} -> B-issuer_tax_id'
  
def recipient_name_to_bio(data):
    json_data = json.loads(data)

    # Extract the recipient name
    recipient_name = json_data['recipient']['name']
    
    recipient_name = recipient_name.split()
    text = textwrap.dedent(f"""
          Datos -> O
          del -> O
          Receptor -> O
          : -> O
          """)
     
    for i, name in enumerate(recipient_name):
        if i == 0:
            text += f"{name} -> B-recipient_name\n"
        else:
            text += f"{name} -> I-recipient_name\n"
    
    return textwrap.dedent(text).strip()


def recipient_address_to_bio(data):
    json_data = json.loads(data)

    # Extract the recipient address
    recipient_address = json_data['recipient']['address']
    
    recipient_address = recipient_address.split()
    text = ""
     
    for i, address in enumerate(recipient_address):
        if i == 0:
            text += f"{address} -> B-recipient_address\n"
        else:
            text += f"{address} -> I-recipient_address\n"
    
    return textwrap.dedent(text).strip()

def recipient_phone_to_bio(data):
    json_data = json.loads(data)

    # Extract the recipient phone
    recipient_phone = json_data['recipient']['phone']

    return f'{recipient_phone} -> B-recipient_phone'
  
def recipient_email_to_bio(data):
    json_data = json.loads(data)

    # Extract the recipient email
    recipient_email = json_data['recipient']['email']

    return f'{recipient_email} -> B-recipient_email'
  
def recipient_tax_id_to_bio(data):
    json_data = json.loads(data)

    # Extract the recipient tax id
    recipient_tax_id = json_data['recipient']['tax_id']

    return f'{recipient_tax_id} -> B-recipient_tax_id'



def item_description_to_bio(data, item_index=0):
    json_data = json.loads(data)

    # Extract the item description
    item = json_data['items'][item_index]
    text = ""

    for i, word in enumerate(item['description'].split()):
        if i == 0:
            text += f"{word} -> B-item_description\n"
        else:
            text += f"{word} -> I-item_description\n"
    
    return textwrap.dedent(text).strip()

def item_quantity_to_bio(data, item_index=0):
    json_data = json.loads(data)

    # Extract the item quantity
    item = json_data['items'][item_index]
    item_quantity = item['quantity']

    return f'{item_quantity} -> B-item_quantity'
  
def item_unit_price_to_bio(data, item_index=0):
    json_data = json.loads(data)

    # Extract the item unit price
    item = json_data['items'][item_index]
    item_unit_price = item['unit_price']

    return f'{item_unit_price} -> B-item_unit_price'

def item_total_to_bio(data, item_index=0):
    json_data = json.loads(data)

    # Extract the item total
    item = json_data['items'][item_index]
    item_total = item['total']

    return f'{item_total} -> B-item_total'

def subtotal_to_bio(data):
    json_data = json.loads(data)
    
    subtotal = json_data['subtotal']

    # Extract the subtotal
    text = textwrap.dedent(f"""
          Subtotal -> O
          : -> O
          {round(subtotal,2)} -> B-subtotal""").strip()

    return text

def tax_description_to_bio(data):
    json_data = json.loads(data)

    # Extract the tax description
    tax_description = json_data['taxes'][0]['description']
  

    return f'{tax_description} -> B-tax_description'

def tax_percentage_to_bio(data):
    json_data = json.loads(data)

    # Extract the tax percentage
    tax_percentage = json_data['taxes'][0]['percentage']
    
    text = textwrap.dedent(f"""
                           ({tax_percentage}%) -> B-tax_percentage
                           : -> O
                           """).strip()
    return text

def tax_amount_to_bio(data):
    json_data = json.loads(data)

    # Extract the tax amount
    tax_amount = json_data['taxes'][0]['amount']

    return f'{round(tax_amount,2)} -> B-tax_amount'
  
def total_to_bio(data):
    json_data = json.loads(data)

    # Extract the total
    total = json_data['total']
    
    text = textwrap.dedent(f"""
          Total -> O
          : -> O
          {round(total,2)} -> B-total
          """).strip()

    return text

def payment_method_to_bio(data):
    json_data = json.loads(data)

    # Extract the payment method
    payment_method = json_data['payment_method']
    
    text = textwrap.dedent(f"""
          Método -> O
          de -> O
          pago -> O
          : -> O
          {payment_method} -> B-payment_method
          """).strip()

    return text

def table_header_to_bio():
    text = textwrap.dedent(f"""
        Descripción -> O
        Cantidad -> O
        Precio -> O
        Unitario -> O
        Total -> O
          """).strip()

    return text
  

from abc import ABC, abstractmethod



"""
Alimentacion Salcedo y asociados S.L. Acceso Amarilis Feijoo 42 Palencia, 09474 +34945094847 gfonseca@ocana es SGK487UbO523
FACTURA
Datos del ciente: Nando Rico Nino Camino Melisa Roca 36 Almeria, 26586 +34928408955 hgallardo@yahoo.com tix414bei004
No FACTURA: FECHA:
881785 2024-05-22
CANTIDAD
DESCRIPCION
PRECIO UNITARIO
TOTAL
5
matrix interactive convergence
31.20
156.00
6
grow one-to-one models
32.79
196.74
Subtotal: VAT (16%): TOTAL:
352.74 56.44 409.18
"""

import json
import textwrap

def format_tokens(text, label_prefix):
    tokens = text.split()
    formatted = ""
    for i, token in enumerate(tokens):
        if i == 0:
            formatted += f"{token} -> B-{label_prefix}\n"
        else:
            formatted += f"{token} -> I-{label_prefix}\n"
    return formatted.strip()

def schema_structure1(data):
    json_data = json.loads(data)

    text = textwrap.dedent(f"""
{format_tokens(json_data['issuer']['name'], 'issuer_name')}
{format_tokens(json_data['issuer']['address'].strip(), 'issuer_address')}
{json_data['issuer']['phone']} -> B-issuer_phone
{json_data['issuer']['email']} -> B-issuer_email
{json_data['issuer']['tax_id']} -> B-issuer_tax_id
FACTURA -> O                         
Datos -> O
del -> O
cliente -> O
: -> O
{format_tokens(json_data['recipient']['name'], 'recipient_name')}
{format_tokens(json_data['recipient']['address'].strip(), 'recipient_address')}
{json_data['recipient']['phone']} -> B-recipient_phone
{json_data['recipient']['email']} -> B-recipient_email
{json_data['recipient']['tax_id']} -> B-recipient_tax_id
No -> O
FACTURA -> O
: -> O
{json_data['invoice_id']} -> B-invoice_id
FECHA -> O
: -> O
{json_data['issue_date']} -> B-issue_date
CANTIDAD -> O
DESCRIPCION -> O
PRECIO -> O
UNITARIO -> O
TOTAL -> O
    """).strip()

    for item in json_data['items']:
        text += "\n" + textwrap.dedent(f"""
            {item['quantity']} -> B-item_quantity
            {item['description']} -> B-item_description
            {item['unit_price']} -> B-item_unit_price
            {item['total']} -> B-item_total
        """).strip()

    text += f"\nSubtotal -> O \n: -> O\n {json_data['subtotal']} -> B-subtotal"

    for tax in json_data['taxes']:
        text += "\n" + textwrap.dedent(f"""
            {tax['description']} -> B-tax_description
            ({tax['percentage']}%) -> B-tax_percentage
            : -> O
            {tax['amount']} -> B-tax_amount
        """).strip()

    text += "\n" + textwrap.dedent(f"""
        TOTAL -> O
        : -> O
        {json_data['total']} -> B-total
    """).strip()
    
    return text

def schema_structure2(data):
    json_data = json.loads(data)

    text = textwrap.dedent(f"""
{format_tokens(json_data['issuer']['name'], 'issuer_name')}
{format_tokens(json_data['issuer']['address'].strip(), 'issuer_address')}
{json_data['issuer']['phone']} -> B-issuer_phone
{json_data['issuer']['email']} -> B-issuer_email
{json_data['issuer']['tax_id']} -> B-issuer_tax_id
Cliente -> O
: -> O
{format_tokens(json_data['recipient']['name'], 'recipient_name')}
{format_tokens(json_data['recipient']['address'].strip(), 'recipient_address')}
{json_data['recipient']['phone']} -> B-recipient_phone
{json_data['recipient']['email']} -> B-recipient_email
{json_data['recipient']['tax_id']} -> B-recipient_tax_id
No -> O
FACTURA -> O
: -> O
{json_data['invoice_id']} -> B-invoice_id
FECHA -> O
: -> O
{json_data['issue_date']} -> B-issue_date
PAGADO -> O
CON -> O
: -> O
{json_data['payment_method']} -> B-payment_method
CANTIDAD -> O
DESCRIPCION -> O
PRECIO -> O
UNITARIO -> O
TOTAL -> O
    """).strip()

    for item in json_data['items']:
        text += "\n" + textwrap.dedent(f"""
            {item['quantity']} -> B-item_quantity
            {item['description']} -> B-item_description
            {item['unit_price']} -> B-item_unit_price
            {item['total']} -> B-item_total
        """).strip()

    text += f"\nSubtotal -> O\n: -> O\n {json_data['subtotal']} -> B-subtotal"

    for tax in json_data['taxes']:
        text += "\n" + textwrap.dedent(f"""
            {tax['description']} -> B-tax_description
            ({tax['percentage']}%) -> B-tax_percentage
            : -> O
            {tax['amount']} -> B-tax_amount
        """).strip()

    text += "\n" + textwrap.dedent(f"""
        TOTAL -> O
        : -> O
        {json_data['total']} -> B-total
    """).strip()
    
    return text

def schema_structure3(data):
    json_data = json.loads(data)

    text = textwrap.dedent(f"""
Invoice -> O
{json_data['invoice_id']} -> B-invoice_id
Issue -> O
Date -> O
: -> O
{json_data['issue_date']} -> B-issue_date
Due -> O
Date -> O
: -> O
{json_data['due_date']} -> B-due_date
Issuer -> O
Details -> O
: -> O
{format_tokens(json_data['issuer']['name'], 'issuer_name')}
{format_tokens(json_data['issuer']['address'].strip(), 'issuer_address')}
{json_data['issuer']['phone']} -> B-issuer_phone
{json_data['issuer']['email']} -> B-issuer_email
{json_data['issuer']['tax_id']} -> B-issuer_tax_id
Recipient -> O
Details -> O
: -> O
{format_tokens(json_data['recipient']['name'], 'recipient_name')}
{format_tokens(json_data['recipient']['address'].strip(), 'recipient_address')}
{json_data['recipient']['phone']} -> B-recipient_phone
{json_data['recipient']['email']} -> B-recipient_email
{json_data['recipient']['tax_id']} -> B-recipient_tax_id
Description -> O
Quantity -> O
Unit -> O
Price -> O
Total -> O
    """).strip()

    for item in json_data['items']:
        text += "\n" + textwrap.dedent(f"""
            {item['description']} -> B-item_description
            {item['quantity']} -> B-item_quantity
            {item['unit_price']} -> B-item_unit_price
            {item['total']} -> B-item_total
        """).strip()

    text += f"\nSubtotal -> O\n : -> O\n {json_data['subtotal']} -> B-subtotal"

    for tax in json_data['taxes']:
        text += "\n" + textwrap.dedent(f"""
            {tax['description']} -> B-tax_description
            ({tax['percentage']}%) -> B-tax_percentage
            : -> O
            {tax['amount']} -> B-tax_amount
        """).strip()

    text += "\n" + textwrap.dedent(f"""
        Total -> O
        : -> O
        {json_data['total']} -> B-total
        Payment -> O
        Method -> O
        : -> O
        {json_data['payment_method']} -> B-payment_method
    """).strip()
    
    return text

def schema_structure4(data):
    json_data = json.loads(data)

    text = textwrap.dedent(f"""
Factura -> O
{json_data['invoice_id']} -> B-invoice_id
Fecha -> O
de -> O
emision -> O
: -> O
{json_data['issue_date']} -> B-issue_date
Fecha -> O
de -> O
vencimiento -> O
: -> O
{json_data['due_date']} -> B-due_date
Datos -> O
del -> O
Emisor -> O
: -> O
{format_tokens(json_data['issuer']['name'], 'issuer_name')}
{format_tokens(json_data['issuer']['address'].strip(), 'issuer_address')}
{json_data['issuer']['phone']} -> B-issuer_phone
{json_data['issuer']['email']} -> B-issuer_email
{json_data['issuer']['tax_id']} -> B-issuer_tax_id
Datos -> O
del -> O
Receptor -> O
: -> O
{format_tokens(json_data['recipient']['name'], 'recipient_name')}
{format_tokens(json_data['recipient']['address'].strip(), 'recipient_address')}
{json_data['recipient']['phone']} -> B-recipient_phone
{json_data['recipient']['email']} -> B-recipient_email
{json_data['recipient']['tax_id']} -> B-recipient_tax_id
Descripcion -> O
Cantidad -> O
Precio -> O
Unitario -> O
Total -> O
    """).strip()

    for item in json_data['items']:
        text += "\n" + textwrap.dedent(f"""
            {item['description']} -> B-item_description
            {item['quantity']} -> B-item_quantity
            {item['unit_price']} -> B-item_unit_price
            {item['total']} -> B-item_total
        """).strip()

    text += f"\nSubtotal -> O\n : -> O\n {json_data['subtotal']} -> B-subtotal"

    for tax in json_data['taxes']:
        text += "\n" + textwrap.dedent(f"""
            {tax['description']} -> B-tax_description
            ({tax['percentage']}%) -> B-tax_percentage
            : -> O
            {tax['amount']} -> B-tax_amount
        """).strip()

    text += "\n" + textwrap.dedent(f"""
        Total -> O
        : -> O
        {json_data['total']} -> B-total
        Metodo -> O
        de -> O
        pago -> O
        : -> O
        {json_data['payment_method']} -> B-payment_method
    """).strip()
    
    return text

def schema_structure5(data):
    json_data = json.loads(data)

    text = textwrap.dedent(f"""
FACTURA -> O
Datos -> O
del -> O
cliente -> O
: -> O
CIF -> O
: -> O
{json_data['recipient']['tax_id']} -> B-recipient_tax_id
Telf -> O
: -> O
{json_data['recipient']['phone']} -> B-recipient_phone
Nombre -> O
: -> O
{format_tokens(json_data['recipient']['name'], 'recipient_name')}
Correo -> O
: -> O
{json_data['recipient']['email']} -> B-recipient_email
{format_tokens(json_data['recipient']['address'].strip(), 'recipient_address')}
No -> O
FACTURA -> O
: -> O
{json_data['invoice_id']} -> B-invoice_id
FECHA -> O
: -> O
{json_data['issue_date']} -> B-issue_date
Descripcion -> O
Cantidad -> O
TOTAL -> O
    """).strip()

    for item in json_data['items']:
        text += "\n" + textwrap.dedent(f"""
            {item['description']} -> B-item_description
            {item['quantity']} -> B-item_quantity
            {item['total']} -> B-item_total
        """).strip()

    text += f"\nSubtotal -> O\n : -> O\n {json_data['subtotal']} -> B-subtotal"

    for tax in json_data['taxes']:
        text += "\n" + textwrap.dedent(f"""
            VAT -> O
            ({tax['percentage']}%) -> B-tax_percentage
            : -> O
            {tax['amount']} -> B-tax_amount
        """).strip()

    text += "\n" + textwrap.dedent(f"""
TOTAL -> O
: -> O
{json_data['total']} -> B-total
Forma -> O
de -> O
pago -> O
: -> O
{json_data['payment_method']} -> B-payment_method
Datos -> O
del -> O
Emisor -> O
: -> O
CIF -> O
: -> O
{json_data['issuer']['tax_id']} -> B-issuer_tax_id
Telf -> O
: -> O
{json_data['issuer']['phone']} -> B-issuer_phone
Nombre -> O
: -> O
{format_tokens(json_data['issuer']['name'], 'issuer_name')}
Correo -> O
: -> O
{json_data['issuer']['email']} -> B-issuer_email
{format_tokens(json_data['issuer']['address'].strip(), 'issuer_address')}
    """).strip()
    
    return text


