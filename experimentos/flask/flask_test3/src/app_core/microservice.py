import pkgutil
from types import ModuleType
from typing import Any, List
from flask import Blueprint, Flask
import modules
from app_core import wireup_cotainer

class ModuleInfo:
    def __init__(self, name: str, bp: Blueprint, services:List[Any]=[], service_modules: list[ModuleType] = [], parameters: dict[str, Any] = {}):
        self.name = name
        self.bp = bp
        self.services = services
        self.service_modules = service_modules
        self.parameters = parameters

def init(app:Flask):
    #pkgutil.iter_modules obtiene los modulos en el paquete services
    for _, module_name, _ in pkgutil.iter_modules(modules.__path__):
        #Cargo el modulo
        module = __import__(f'modules.{module_name}', fromlist=['route_info'])

        #Si existe el blueprint lo registro
        if module is not None and "route_info" in module.__dict__:
            if not isinstance(module.route_info, ModuleInfo):continue
            print(f"Registering blueprint: {module.route_info.name}")
            app.register_blueprint(module.route_info.bp)
            wireup_cotainer.add_service(module.route_info.services)
            wireup_cotainer.add_service_module(module.route_info.service_modules)
            wireup_cotainer.add_parameter(module.route_info.parameters)
