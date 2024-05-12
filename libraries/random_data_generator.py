from faker import Faker
import json
from random import randint, uniform

faker = Faker("es_ES")

def generate_item():
    unit_price = "{:.2f}".format(round(uniform(10, 100), 2))
    quantity = randint(1, 10)
    total = "{:.2f}".format(round(float(unit_price) * quantity, 2))
    return {
        "description": faker.bs(),
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

def generate_invoice():
    items = [generate_item() for _ in range(randint(1, 5))]  # Generate between 1 and 5 items
    subtotal = "{:.2f}".format(round(sum(float(item["total"]) for item in items), 2))
    vat_percentage = 16
    vat_amount = "{:.2f}".format(round(float(subtotal) * vat_percentage / 100, 2))
    total = "{:.2f}".format(round(float(subtotal) + float(vat_amount), 2))

    invoice = {
        "invoice_id": faker.unique.random_number(digits=6),
        "issue_date": faker.date_between(start_date="-30d", end_date="today").isoformat(),
        "due_date": faker.date_between(start_date="today", end_date="+30d").isoformat(),
        "issuer": {
            "name": faker.company(),
            "address": faker.address(),
            "phone": faker.phone_number(),
            "email": faker.company_email(),
            "tax_id": faker.bothify(text='???###???###')
        },
        "recipient": {
            "name": faker.name(),
            "address": faker.address(),
            "phone": faker.phone_number(),
            "email": faker.free_email(),
            "tax_id": faker.bothify(text='???###???###')
        },
        "items": items,
        "subtotal": subtotal,
        "taxes": [
            {
                "description": "VAT",
                "percentage": vat_percentage,
                "amount": vat_amount
            }
        ],
        "total": total,
        "payment_method": faker.random_element(elements=("Credit Card", "PayPal", "Bank Transfer")),
        "currency": "EUR"
    }

    return json.dumps(invoice, indent=2)

# Generate and print the fake invoice JSON
