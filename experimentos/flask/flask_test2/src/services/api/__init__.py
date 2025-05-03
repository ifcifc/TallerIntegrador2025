from flask import Blueprint
from core.service import RouteInfo
import services.api.models

#Si no se separa la inicializacion del blueprint de la RouteInfo, python se vuelve loco
_bp = Blueprint('api', __name__, url_prefix='/api')
route_info = RouteInfo('api_service', _bp)

import services.api.api

