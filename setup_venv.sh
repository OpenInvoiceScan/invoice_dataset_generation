#!/bin/bash

# Nombre del entorno virtual
VENV_DIR=".venv"

# Verifica si el entorno virtual ya existe
if [ ! -d "$VENV_DIR" ]; then
    # Crea el entorno virtual
    python3 -m venv $VENV_DIR
    echo "Entorno virtual creado en $VENV_DIR"
fi

# Activa el entorno virtual
source $VENV_DIR/bin/activate

# Lista de dependencias
DEPENDENCIES=(
    "faker"
    "jinja2"
    "weasyprint"
    "pdfkit"
    "beautifulsoup4"
    "pyppeteer"
    "lxml"
)

# Instala las dependencias
for package in "${DEPENDENCIES[@]}"; do
    pip install $package
done

echo "Dependencias instaladas: ${DEPENDENCIES[*]}"

# Desactiva el entorno virtual
deactivate

echo "Script completado."
