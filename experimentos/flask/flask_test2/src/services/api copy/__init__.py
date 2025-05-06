from flask import Blueprint
from core.service import RouteInfo

#Si no se separa la inicializacion del blueprint de la RouteInfo, python se vuelve loco
_bp = Blueprint('api_2', __name__, url_prefix='/api2')
route_info = RouteInfo('api_service', _bp)



@_bp.route("/")
def index():
    return "HOLA"