#!/bin/bash

# Nombre del entorno virtual
VENV_DIR=".venv"

# Crear el entorno virtual
echo "Creando entorno virtual en el directorio $VENV_DIR..."
python3 -m venv $VENV_DIR

# Activar el entorno virtual
echo "Activando el entorno virtual..."
source $VENV_DIR/bin/activate

# Usar el pip dentro del venv para actualizar e instalar
echo "Actualizando pip dentro del entorno virtual..."
$VENV_DIR/bin/pip install --upgrade pip

echo "Instalando Pygame 2.6.0 dentro del entorno virtual..."
$VENV_DIR/bin/pip install pygame==2.6.0

# Confirmar instalación
echo "Confirmando la instalación de Pygame dentro del venv..."
$VENV_DIR/bin/python -c "import pygame; print('Pygame instalado. Versión:', pygame.ver)"

echo "¡Instalación completada en el entorno virtual $VENV_DIR!"
