
import libraries.random_data_generator as rdg
import libraries.template_parser as tp
import json
import os

if __name__ == "__main__":
    rdg.generate_invoice()

    for i in range(10):
        json_data = json.loads(rdg.generate_invoice())
        tp.parse_template(json_data, './invoice_template', 'output/', f'factura{i}.pdf')

