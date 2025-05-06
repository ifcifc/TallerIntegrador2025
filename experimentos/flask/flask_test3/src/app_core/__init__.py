from flask import Flask, json
from flask_jwt_extended import JWTManager
from .wireup_setup import WireupContainer

app = Flask(__name__,                 
            template_folder='../templates',
            static_folder='../static',
            static_url_path='/static')

app.config.from_file("../config.json", load=json.load)
jwt = JWTManager(app)
wireup_cotainer = WireupContainer()

#Se carga aca para evitar las referencias circulares, cosas de python
from .models import *
from app_core.services.usuario_service import UsuarioService
wireup_cotainer.add_service(UsuarioService)