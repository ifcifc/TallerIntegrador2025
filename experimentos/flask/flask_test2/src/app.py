from flask import Flask
from flask_jwt_extended import JWTManager, get_jwt, get_jwt_identity, jwt_required
import database
import route
import json

app = Flask(__name__)
app.config.from_file("../config.json", load=json.load)
jwt = JWTManager(app)

@app.route("/")
@jwt_required(optional=True)
def hello_world():
    current_identity = get_jwt_identity()
    if current_identity:
        claims = get_jwt()
        username = claims["name"]
        return f"<p>Hello, {username}!</p>"
    else:
        return "<p>Hello, World!</p>"

database.init(app)
route.init(app)
database.create_all(app)