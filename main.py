
import libraries.random_data_generator as rdg
import libraries.template_parser as tp
import json
import sys
import os

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print('Usage: python main.py <number_of_invoices> <template_dir> <output_dir>')
        sys.exit(1)


    number_of_invoices = int(sys.argv[1])
    template_dir = sys.argv[2]
    output_dir = sys.argv[3]

    if output_dir[-1] != '/':
        output_dir = output_dir + '/'


    for i in range(number_of_invoices):
        json_data = json.loads(rdg.generate_invoice())
        tp.parse_template(json_data, template_dir, output_dir, f'factura{i}.pdf')
        #Save the json data to a file
        with open(f'{output_dir}/factura{i}.json', 'w') as f:
            json.dump(json_data, f, indent=2)

