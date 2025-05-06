from types import SimpleNamespace

from flask import jsonify, request
import requests

from app_core import app
from app_core.security.decorators.permissions import api_access

_proxies = {
    "dinosaurs": SimpleNamespace(api_url="https://dinosaur-facts-api.shultzlab.com/dinosaurs", all_paths=False, is_public=True, access_permissions={}),
    "dinosaurs/random": SimpleNamespace(api_url="https://dinosaur-facts-api.shultzlab.com/dinosaurs", all_paths=False, is_public=False, access_permissions={"root.index"}),
    "cat": SimpleNamespace(api_url="https://catfact.ninja", all_paths=True, is_public=True, access_permissions={}),
}

def proxy_services(path:str):
    return _proxies.get(path, None)

def exist_route(path:str):
    return path in _proxies

@app.route('/service/<service>/', defaults={'path': None}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/service/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@api_access(is_public=True)
def gateway(service, path):
    endpoint = request.path.removeprefix("/service/").rstrip("/")
    proxy_endpoint = proxy_services(endpoint)
    if proxy_endpoint is None:
        proxy_endpoint = proxy_services(service)

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

    return jsonify(response.json()), response.status_code