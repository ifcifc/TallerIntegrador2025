import pkgutil
from flask import Blueprint

import routes

class RouteInfo:
    def __init__(self, name: str, bp: Blueprint):
        self.name = name
        self.bp = bp


def init(app):
    #pkgutil.iter_modules obtiene los modulos en el paquete routes
    for _, module_name, _ in pkgutil.iter_modules(routes.__path__):
        #Cargo el modulo
        module = __import__(f'routes.{module_name}', fromlist=['route_info'])

        #Si existe el blueprint lo registro
        if module.route_info:
            if not isinstance(module.route_info, RouteInfo):continue
            print(f"Registering blueprint: {module.route_info.name}")
            app.register_blueprint(module.route_info.bp)
