from flask import Blueprint, render_template
from core.route import RouteInfo
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

#Si no se separa la inicializacion del blueprint de la RouteInfo, python se vuelve loco
_bp = Blueprint('simple_login', __name__, 
                url_prefix='/',  
                template_folder='templates',
                static_folder='static',
                static_url_path='/simple_login/static')
route_info = RouteInfo('simple_login', _bp)

@_bp.route("/hello")
@jwt_required(optional=True)
def hello_world():
    current_identity = get_jwt_identity()
    if current_identity:
        claims = get_jwt()
        username = claims["name"]
        return f"<p>Hello, {username}!</p>"
    else:
        return "<p>Hello, World!</p>"

@_bp.route("/")
def index():
    return render_template("index_admin.html")

