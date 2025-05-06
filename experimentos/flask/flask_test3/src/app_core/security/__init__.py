from flask import abort, request
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from app_core import app, wireup_cotainer
from .gateway import get_service
from .services.jwt_token_service import JwtTokenService

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

wireup_cotainer.add_service(JwtTokenService)


def init():
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["100 per minute", "10 per second"],
        storage_uri="memory://")

    @app.before_request
    @jwt_required(optional=True)
    def authenticate_request():
        endpoint = request.endpoint
        
        if request.path.startswith("/service/"):
            path = request.path.removeprefix("/service/")
            proxy_service = get_service(path)
            if proxy_service is None and path:
                service, _ = path.split('/',1)
                proxy_service = get_service(service.rstrip("/"))
                if (not proxy_service is None) and (not proxy_service.all_paths):
                    abort(401, description=f"El endpoint <{path}> no es publico")

            if not proxy_service is None:
                limiter.enabled = proxy_service.limiter or False
                verify(proxy_service)
            else:
                abort(404, description=f"Servicio desconocido {request.path}")
        elif endpoint is None:
            abort(404, description=f"Endpoint desconocido {request.path}")
        else:
            view_func = app.view_functions.get(endpoint)
            if hasattr(view_func, "_security_metadata"):
                meta = view_func._security_metadata
                verify(meta)
            else:
                abort(401, description=f"El endpoint <{endpoint}> no es publico")

def verify(meta):
    if not meta.is_public:
        identity = get_jwt_identity()
        if identity:
            if meta.access_permissions:
                jwt_data = get_jwt()
                jwt_s:JwtTokenService = wireup_cotainer.container.get(JwtTokenService)

                jwt_meta = jwt_s.get_token_meta(jwt_data)

                #Compruebo si el usuario tiene los permisss para acceder al endpoint
                if (not "admin" in jwt_meta["perms"]) and not jwt_meta["perms"].issuperset(meta.access_permissions):
                    abort(401, description=f"Acceso no autorizado, Usted no tiene los permisos para acceder a este sitio")
        else:
            abort(401, description=f"Acceso no autorizado, falta token de acceso")
        
    