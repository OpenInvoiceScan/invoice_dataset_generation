import os
import base64
import re

def file_to_base64(filepath):
    with open(filepath, "rb") as file:
        encoded_data = base64.b64encode(file.read()).decode('utf-8')
    return encoded_data

def embed_fonts_in_css(css_string, template_base_dir):
    # Define una expresión regular para encontrar los `@font-face` y `url(...)`
    url_pattern = re.compile(r"url\((.*?)\)", re.IGNORECASE)
    
    def replace_url_with_base64(match):
        relative_path = match.group(1).strip("'\" ")
        full_path = os.path.join(template_base_dir, relative_path)
        
        if os.path.exists(full_path):
            file_extension = os.path.splitext(full_path)[1][1:].lower()
            mime_type = f"font/{file_extension}" if file_extension != "svg" else "image/svg+xml"
            base64_data = file_to_base64(full_path)
            return f"url('data:{mime_type};base64,{base64_data}')"
        else:
            print(f"Advertencia: No se encontró el archivo {full_path}")
            return match.group(0)  # Devolver la ruta original si el archivo no existe
    
    # Reemplazar todas las rutas `url(...)` por su equivalente en base64
    css_string = url_pattern.sub(replace_url_with_base64, css_string)
    
    return css_string