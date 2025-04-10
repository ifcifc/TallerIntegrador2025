import platform
from flask import Blueprint, jsonify
import platform
import os
# Crea un blueprint para las rutas relacionadas con "home"
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
    return jsonify({
        'name': 'api test 1',
        'date': '090425'
    })

@bp.route('/hw')
def hw():
    return jsonify({
    "sistema_operativo": platform.system(),
    "version_os": platform.version(),
    "nombre_maquina": platform.node(),
    "arquitectura": platform.architecture()[0],
    "procesador": platform.processor(),
    "cpu_cores": os.cpu_count()
    })
