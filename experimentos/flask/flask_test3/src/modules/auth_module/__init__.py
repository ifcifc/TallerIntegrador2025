from flask import Blueprint, make_response
from flask_jwt_extended import set_access_cookies
from wireup import Injected

from app_core.models.usuario_model import UsuarioModel
from app_core.module_loader import ModuleInfo
from app_core.security.decorators.permissions import api_access
from app_core.security.services.jwt_token_service import JwtTokenService
from app_core.services.usuario_service import UsuarioService

#Si no se separa la inicializacion del blueprint de la RouteInfo, python se vuelve loco
_bp = Blueprint('auth', __name__, url_prefix='/auth')
route_info = ModuleInfo('auth_module', _bp)


@_bp.route("/")
@api_access(is_public=False, access_permissions={"root.index"})
def hello_world(usuarios: Injected[UsuarioService]):
    return usuarios.get_all(True)

@_bp.route("/login")
@api_access(is_public=True)
def login(jwt_token_service: Injected[JwtTokenService], usuarios: Injected[UsuarioService]):
    usuario:UsuarioModel = usuarios.get_by_email("admin")
    
    access_token = jwt_token_service.create_access_token(id_usuario=usuario.id, perms=usuario.get_permissions(), identity=str(usuario.id))
    response=make_response("login :3")
    set_access_cookies(response, access_token)
    return response, 200