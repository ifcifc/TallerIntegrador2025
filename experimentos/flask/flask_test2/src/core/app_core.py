from flask import Flask, json
from flask_jwt_extended import JWTManager
from core.wireup_container import WireupContainer


app = Flask(__name__,                 
            template_folder='../templates',
            static_folder='../static',
            static_url_path='/static')

app.config.from_file("../../config.json", load=json.load)
jwt = JWTManager(app)
wireup_cotainer = WireupContainer()