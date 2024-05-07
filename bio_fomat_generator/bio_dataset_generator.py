import libraries.random_data_generator as rdg
import libraries.bio_text_parser as btp
import json

def invoice_id_chunk(json_input):
    return btp.invoice_id_to_bio(json_input)

def date_chunk(json_input):
    return btp.issue_date_to_bio(json_input) + "\n" +  btp.due_date_to_bio(json_input)

def issuer_data_chunk(json_input):
    text = btp.issuer_name_to_bio(json_input)
    text += "\n" + btp.issuer_address_to_bio(json_input)
    text += "\n" + btp.issuer_phone_to_bio(json_input)
    text += "\n" + btp.issuer_email_to_bio(json_input)
    text += "\n" + btp.issuer_tax_id_to_bio(json_input)
    return text

def recipient_data_chunk(json_input):
    text = btp.recipient_name_to_bio(json_input)
    text += "\n" + btp.recipient_address_to_bio(json_input)
    text += "\n" + btp.recipient_phone_to_bio(json_input)
    text += "\n" + btp.recipient_email_to_bio(json_input)
    text += "\n" + btp.recipient_tax_id_to_bio(json_input)
    return text

def item_row_chunk(json_input, index = 0):
    return btp.item_description_to_bio(json_input, index) + "\n" + btp.item_quantity_to_bio(json_input, index) + "\n" + btp.item_unit_price_to_bio(json_input, index) + "\n" + btp.item_total_to_bio(json_input, index)

def full_items_chunk(json_input):
    loaded_json = json.loads(json_input)
    text = btp.table_header_to_bio() + "\n"
    for i in range(len(loaded_json['items'])):
        text += item_row_chunk(json_input, i) + "\n"
    return text

def total_chunk(json_input):
    text = btp.subtotal_to_bio(json_input)
    text += "\n" + btp.tax_description_to_bio(json_input) + "\n" + btp.tax_percentage_to_bio(json_input) + "\n" + btp.tax_amount_to_bio(json_input)
    text += "\n" + btp.total_to_bio(json_input)
    return text

def payment_method_chunk(json_input):
    return btp.payment_method_to_bio(json_input)



def generate_full_bio_text(json_input):
    text = invoice_id_chunk(json_input) + "\n"
    text += date_chunk(json_input) + "\n"
    text += issuer_data_chunk(json_input) + "\n"
    text += recipient_data_chunk(json_input) + "\n"
    text += full_items_chunk(json_input) + "\n"
    text += total_chunk(json_input) + "\n"
    text += payment_method_chunk(json_input)
    return text

def generate_both_information(json_input):
    return json_input + "\n" + generate_full_bio_text(json_input)



if __name__ == "__main__":
    directory = "dataset_output/train/"
    for i in range(1000):
        json_input = rdg.generate_invoice()
        selector = i % 8
        file_name = f"train{i}.tokens"
        with open(directory + file_name, 'w') as file:
            if selector == 0:
                file.write(invoice_id_chunk(json_input) + '\n')
            elif selector == 1:
                file.write(date_chunk(json_input) + '\n')
            elif selector == 2:
                file.write(issuer_data_chunk(json_input) + '\n')
            elif selector == 3:
                file.write(recipient_data_chunk(json_input) + '\n')
            elif selector == 4:
                file.write(full_items_chunk(json_input) + '\n')
            elif selector == 5:
                file.write(total_chunk(json_input) + '\n')
            elif selector == 6:
                file.write(payment_method_chunk(json_input) + '\n')
            elif selector == 7:
                file.write(generate_full_bio_text(json_input) + '\n')