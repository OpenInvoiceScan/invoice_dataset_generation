import libraries.random_data_generator as rdg
import libraries.bio_text_parser as btp
import json


if __name__ == "__main__":
    directory = "dataset_output/train/"
    for i in range(1000):
        json_input = rdg.generate_invoice()
        selector = i % 8
        file_name = f"train{i}.tokens"
        with open(directory + file_name, 'w') as file:
            if selector == 0:
                file.write(btp.schema_structure1(json_input) + '\n')
            elif selector == 1:
                file.write(btp.schema_structure2(json_input) + '\n')
            elif selector == 2:
                file.write(btp.schema_structure3(json_input) + '\n')
            elif selector == 3:
                file.write(btp.schema_structure4(json_input) + '\n')
            elif selector == 4:
                file.write(btp.schema_structure5(json_input) + '\n')