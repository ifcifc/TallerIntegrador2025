from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import set_access_cookies
from marshmallow import ValidationError
from wireup import Injected

from app_core.models.usuario_model import UsuarioModel
from app_core.module_loader import ModuleInfo
from app_core.schemas.signup_schema import SignupSchema
from app_core.security.decorators.permissions import api_access
from app_core.security.services.jwt_token_service import JwtTokenService
from app_core.services.usuario_service import UsuarioService

#Si no se separa la inicializacion del blueprint de la RouteInfo, python se vuelve loco
_bp = Blueprint('auth', __name__, url_prefix='/auth')
route_info = ModuleInfo('auth_module', _bp)
signup_schema = SignupSchema()

@_bp.route("/")
@api_access(is_public=False, access_permissions={"root.index"})
def hello_world(usuarios: Injected[UsuarioService]):
    return usuarios.get_all(True)

@_bp.route("/login", methods=["POST"])
@api_access(is_public=True)
def login(jwt_token_service: Injected[JwtTokenService], usuarios: Injected[UsuarioService]):
    usuario:UsuarioModel = usuarios.get_by_email("admin")
    
    access_token = jwt_token_service.create_access_token(id_usuario=usuario.id, perms=usuario.get_permissions(), identity=str(usuario.id))
    response=make_response(jsonify({"access_token":access_token}))
    set_access_cookies(response, access_token)
    return response, 200

@_bp.route("/signup", methods=["POST"])
@api_access(is_public=True)
def signup(usuarios: Injected[UsuarioService]):
    try: 
        json = request.get_json()
        result = signup_schema.load(json)

        usuario = usuarios.get_by_email(result["email"])

        if not usuario is None:
            return jsonify({
                "error":"El email ya esta en uso"
            }), 400

        usuario = usuarios.get_by_nick(result["nick"])

        if not usuario is None:
            return jsonify({
                "error":"El nombre de usuario ya esta en uso"
            }), 400
        
        new_usuario = UsuarioModel(name=result["nick"], email=result["email"], password=result["password"])
        usuarios.create(new_usuario)
        return jsonify(result), 200
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400