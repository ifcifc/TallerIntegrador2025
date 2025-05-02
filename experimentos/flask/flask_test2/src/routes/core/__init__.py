from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token, set_access_cookies
from route import RouteInfo
from routes.core.models.usuario_model import LoginSchema, UsuarioModel
from routes.core.service.usuario_service import UsuarioService

_bp = Blueprint('auth', __name__, url_prefix='/auth')
route_info = RouteInfo('auth_service', _bp)

login_schema = LoginSchema()

@_bp.route('/')
def index():
    UsuarioService.create(UsuarioModel(name='test',email="algo@malgo.com", password="123456"))
    return jsonify(UsuarioService.get_all(True))

@_bp.route('/login')
def login():
    login_data:LoginSchema = login_schema.load(request.args)

    query:UsuarioModel = UsuarioService.get_by_email(login_data['email'])
    
    if not query:
        return jsonify({"error": "User not found", "email":login_data["email"]}), 404
    
    if not query.verify_password(login_data['password']):
        return jsonify({"error": "Invalid password"}), 401

    access_token = create_access_token(identity=str(query.id), additional_claims={
        'name': query.name,
        'email': query.email
    })

    # Crear respuesta con JWT en cookie
    response = jsonify(mensaje="Login exitoso")
    set_access_cookies(response, access_token)
    return response, 200
