from flask import Flask, abort, jsonify, request
from functools import wraps
from typing import Set
from types import SimpleNamespace
import requests

#aparte de flask requiere de requests, para instalar
#pip install requests

#Esto es un ejemplo sencillo de un microservicio enviando la informacion de sus endpoints

#Decorador para poder añadir los permisos como metadatos a la ruta
#Un poco compleja debido a como funciona flask
def api_access(is_public:bool=False, access_permissions:Set[str]=[]):

    def decorator(f):
        # Guardar los metadatos en la función, puede ser un diccionario sencillo
        f._security_metadata = SimpleNamespace(is_public=is_public, access_permissions=set(access_permissions))
        
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
            
        # Copiar los metadatos a la función decorada
        decorated_function._security_metadata = f._security_metadata
        return decorated_function
        
    return decorator


app = Flask(__name__)


#Define un endpoint publica
@app.route("/test1")
@api_access(is_public=True)
def test1():
    return "test1"

#Define un endpoint privado con el requerimiento de permiso de "root.test2"
@app.route("/test2")
@api_access(is_public=False, access_permissions={"root.test2"})
def test2():
    return "test2"

#Este seria el endpoint que usaria el gateway para recuperar la lista de los endpoints del microservicio
@app.route("/endpoint_list")
def endpoint_list():
    endpoints = []
    #Recorro la lista de endpoint del servicio
    for rule in app.url_map.iter_rules():
        #Recupero el metodo del endpoint
        view_func = app.view_functions[rule.endpoint]
        #Si no tiene el atributo _security_metadata lo omito
        if not hasattr(view_func, "_security_metadata"): continue

        #Armo un json con los metadatos del endpoint para el gateway

        endpoints.append({
            "endpoint": rule.endpoint,
            "is_public": view_func._security_metadata.is_public,
            "access_permissions": list(view_func._security_metadata.access_permissions)
        })

    return jsonify(endpoints)

@app.route("/")
def index():
    return """
        <a href='/endpoint_list'>Esto seria lo que recibe el gateway desde el microservicio</a><br>
        <a href='/service/test/test1'>Gateway Endpoint test1</a><br>
        <a href='/service/test/test2'>Gateway Endpoint test2</a><br>
        <a href='/service/test/test3'>Gateway Endpoint test3 (no existe)</a>
    """
#############################################################3

#Esto estaria en el core seria el gateway

#Esta seria la tabla con la referencia a los servicios
_microservice_list = [{
    "nombre":"test",
    "service_url": "http://localhost:5000/"
}]

#Esto seria un metodo para recuperar la lista de enpoints
def get_endpoints():
    endpoints = {}
    #Recorre la lista de microservicios
    for service in _microservice_list:
        #Le pide los endpoints
        #Esto entra a un endpoint especializado del microservicio "endpoint_list"
        response = requests.get(f"{service["service_url"]}/endpoint_list")
        #Aca abria que añdir un de comprobaciones antes que esto
        #Recupero la respuesta
        response_json = response.json()

        service_endpoints={}

        #Recorro la lista de enpoints
        for endpoint in response_json:
            #Obtengo la ruta de acceso
            endpoint_rute = endpoint["endpoint"]

            service_endpoints[endpoint_rute]={
                "url": f"{service["service_url"]}/{endpoint_rute}",
                "is_public":endpoint["is_public"],
                "access_permissions":endpoint["access_permissions"]
            }

        endpoints[service["nombre"]]=service_endpoints

    return endpoints

#Esto toma todo lo que entre por service por cualquier metodo
@app.route('/service/<service>/', defaults={'path': "/"}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/service/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    #Aca esta la lista de enpoints, esto deberia de estar y precargado, no haciendo la peticion
    #cada vez que se accede al gateway
    endpoints = get_endpoints()
    #verifico si existe el servicio
    if not service in endpoints:
        abort(404, description=f"Servicio desconocido {request.path}")

    #verifico si existe el endpoint
    microservice = endpoints[service]
    
    #elimina la ultima </> de la url
    path = path.rstrip("/")

    if not path in microservice:
        abort(404, description=f"Endpoint desconocido {request.path}")

    #Obtengo el enpoint
    endpoint = microservice[path]

    #se remueve el parametro 'Host' y el 'Accept-Encoding' de los headers, para evitar errores
    headers = {key: value for key, value in request.headers if key != "Host" and key != "Accept-Encoding"}
    #Armo la request para enviar al microservicio con todos los datos recibidos
    _request = {
        "url":endpoint["url"], #Esta es la url donde esta alojado el endpoint del microservicio
        "headers": headers,
        "params":request.args,
        "json":request.get_json() if request.is_json else None,
        "data":request.form if not request.is_json else None
    }

    #Este caso esta simplificado solo reenvia get
    #Envia los datos al endpoint del microservicio
    #Esto es el equivalente del ferch de javascript
    response = requests.get(**_request)

    #Devuelvo la respuesta del microservicio
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)