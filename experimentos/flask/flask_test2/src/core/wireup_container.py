from flask import Flask
import wireup
import wireup.integration
import wireup.integration.flask

class WireupContainer:
    container: wireup.SyncContainer
    def __init__(self):
        self.services = []
        self.service_modules = []
        self.parameters = {}

    def add_service(self, service):
        if type(service) is list:
            self.services.extend(service)
        else:
            self.services.append(service)

    def add_service_module(self, service_module):
        if type(service_module) is list:
            self.service_modules.extend(service_module)
        else:
            self.service_modules.append(service_module)
            
    def add_parameter(self, parameter):
        if type(parameter) is dict:
            self.parameters.update(parameter)
        else:
            raise TypeError("Parameter must be a dictionary")

    def init(self, app:Flask):
        # Creación del contenedor de Wireup y registro de servicios
        self.container = wireup.create_sync_container(services=self.services, service_modules=self.service_modules)
        
        # Integración de Wireup con Flask
        
        wireup.integration.flask.setup(self.container, app)
