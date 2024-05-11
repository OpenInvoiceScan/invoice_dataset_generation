import base64
import os
from bs4 import BeautifulSoup

# Función para convertir un archivo a base64
def file_to_base64(filepath):
    with open(filepath, "rb") as file:
        encoded_bytes = base64.b64encode(file.read())
    return encoded_bytes.decode("utf-8")

# Procesar todos los elementos con atributo `src`
def file_to_base64(filepath):
    with open(filepath, "rb") as file:
        encoded_bytes = base64.b64encode(file.read())
    return encoded_bytes.decode("utf-8")

# Función para reemplazar las imágenes en el HTML con su versión en base64
def embed_images_in_html(html_string, template_base_dir):
    soup = BeautifulSoup(html_string, "lxml")

    # Procesar todos los elementos con atributo `src`
    for tag in soup.find_all(src=True):
        src_relative_path = tag['src']
        src_full_path = os.path.join(template_base_dir, src_relative_path)

        if os.path.exists(src_full_path):  # Asegura que el archivo existe en el directorio base
            file_extension = os.path.splitext(src_full_path)[1][1:]
            if file_extension.lower() == "svg":
                mime_type = "image/svg+xml"
            else:
                mime_type = f"image/{file_extension}"

            base64_data = file_to_base64(src_full_path)
            tag['src'] = f"data:{mime_type};base64,{base64_data}"
        else:
            print(f"Advertencia: No se encontró el archivo {src_full_path}")

    return str(soup)
