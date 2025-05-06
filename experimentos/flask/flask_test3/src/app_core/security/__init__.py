from types import SimpleNamespace
from flask import abort, request
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from app_core import app, wireup_cotainer
from app_core.security.services.jwt_token_service import JwtTokenService

wireup_cotainer.add_service(JwtTokenService)

def proxy_services(path:str):
    proxies = {
        "/": SimpleNamespace(api="http://127.0.0.1:5001", is_public=True, access_permissions={})
    }
    return proxies.get(path, None)

def init():
    @app.before_request
    @jwt_required(optional=True)
    def authenticate_request():
        endpoint = request.endpoint
        if endpoint is None:
            proxy_service = proxy_services(request.pat)
            if proxy_service:
                pass
            else: 
                abort(404, description=f"Endpoint desconocido {request.path}")
        
        view_func = app.view_functions.get(endpoint)
        if hasattr(view_func, "_security_metadata"):
            meta = view_func._security_metadata
            verify(meta)


def verify(meta):
    if not meta.is_public:
        identity = get_jwt_identity()
        if identity:
            if meta.access_permissions:
                jwt_data = get_jwt()
                jwt_s:JwtTokenService = wireup_cotainer.container.get(JwtTokenService)

                jwt_meta = jwt_s.get_token_meta(jwt_data)
                
                #Compruebo si el usuario tiene los permisss para acceder al endpoint
                if not jwt_meta["perms"].issuperset(meta.access_permissions):
                    abort(401, description=f"Acceso no autorizado, Usted no tiene los permisos para acceder a este sitio")
        else:
            abort(401, description=f"Acceso no autorizado, falta token de acceso")
        
    else:
        abort(401, description=f"El endpoint <{endpoint}> no es publico")