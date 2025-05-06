from types import SimpleNamespace

from flask import jsonify, request
import requests

from app_core import app
from app_core.security.decorators.permissions import api_access

_services_route = {
    "dinosaurs": SimpleNamespace(api_url="https://dinosaur-facts-api.shultzlab.com/dinosaurs", limiter=True, all_paths=True, is_public=True, access_permissions={}),
    "dinosaurs/random": SimpleNamespace(api_url="https://dinosaur-facts-api.shultzlab.com/dinosaurs", limiter=True, all_paths=False, is_public=False, access_permissions={"root.index"}),
    "cat": SimpleNamespace(api_url="https://catfact.ninja", limiter=False, all_paths=True, is_public=True, access_permissions={}),
    "duckduckgo": SimpleNamespace(api_url="https://lite.duckduckgo.com/lite", limiter=True, all_paths=True, is_public=True, access_permissions={}),
    "internal": SimpleNamespace(api_url="http://127.0.0.1:8033", limiter=False, all_paths=True, is_public=True, access_permissions={}),
    "internal/static": SimpleNamespace(api_url="http://127.0.0.1:8033", limiter=False, all_paths=True, is_public=True, access_permissions={}),
    "internal/api/hw": SimpleNamespace(api_url="http://127.0.0.1:8033", limiter=True, all_paths=True, is_public=False, access_permissions={}),
}

def get_service(path:str):
    return _services_route.get(path, None)

def has_service(path:str):
    return path in _services_route


@app.route('/service', methods=['GET', 'POST'])
@api_access(is_public=False, access_permissions={"admin"})
def index():
    return jsonify([{
          "route":k,
          "api_url":v.api_url, 
          "limiter":v.limiter, 
          "all_paths":v.all_paths, 
          "is_public":v.is_public, 
          "access_permissions":tuple(v.access_permissions)
    } for k,v in _services_route.items()])

@app.route('/service/<service>/', defaults={'path': None}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/service/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@api_access(is_public=True)
def gateway(service, path):
    endpoint = request.path.removeprefix("/service/").rstrip("/")
    proxy_endpoint = get_service(endpoint)
    if proxy_endpoint is None:
        proxy_endpoint = get_service(service)

    target_url = proxy_endpoint.api_url

    if not path is None: target_url=f"{target_url}/{path}"

    #se remueve el parametro 'Host' de los headers
    headers = {key: value for key, value in request.headers if key != "Host" and key != "Accept-Encoding"}

    _request = {
        "url":target_url, 
        "headers": headers,
        "params":request.args,
        "json":request.get_json() if request.is_json else None,
        "data":request.form if not request.is_json else None
    }

    if request.method == 'GET':
        response = requests.get(**_request)
    elif request.method == 'POST':
        response = requests.post(**_request)
    elif request.method == 'PUT':
        response = requests.put(**_request)
    elif request.method == 'DELETE':
        response = requests.delete(**_request)

    return response.content, response.status_code

