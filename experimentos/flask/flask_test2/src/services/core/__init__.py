from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, set_access_cookies, unset_jwt_cookies
from wireup import Injected
from core.service import RouteInfo
from services.core.models.usuario_model import LoginSchema, UsuarioModel, UsuarioModelSchema
from services.core.service.jwt_token_service import JwtTokenService
from services.core.service.usuario_service import UsuarioService

_bp = Blueprint('auth', __name__, url_prefix='/auth')
route_info = RouteInfo('auth_service', _bp, services=[UsuarioService, JwtTokenService])

login_schema = LoginSchema()
usuario_model_schema = UsuarioModelSchema()


@_bp.route('/', methods=['GET'])
def index(usuario_service: Injected[UsuarioService]):
    return jsonify(usuario_service.get_all(True)), 200

@_bp.route('/login', methods=['POST'])
def login(usuario_service: Injected[UsuarioService], jwt_token_service: Injected[JwtTokenService]):
    login_data = login_schema.load(request.json)

    query = usuario_service.get_by_email(login_data['email'])
    
    if not query:
        return jsonify({"error": "Usuario no encontrado", "email": login_data["email"]}), 404

    if not query.verify_password(login_data['password']):
        return jsonify({"error": "Contraseña inválida"}), 401

    tokens = jwt_token_service.get_tokens_by_user(query.id)
    #Solo un token por usuario
    if len(tokens) > 0:
        # Revocar tokens existentes
        for token in tokens:
            jwt_token_service.revoke_token(token)


    access_token = jwt_token_service.create_access_token(id_usuario=query.id, identity=str(query.id), additional_claims={
        'name': query.name,
        'email': query.email
    })

    # Crear respuesta con JWT en cookie
    response = jsonify(mensaje="Login exitoso", usuario={
        'id': str(query.id),
        'name': query.name,
        'email': query.email,
        'token': access_token
    })
    set_access_cookies(response, access_token)
    return response, 200

@_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout(jwt_token_service: Injected[JwtTokenService]):
    jwt_data = get_jwt()
    response = jsonify({"mensaje": "Logout exitoso"})
    
    jwt_token_service.revoke_token(jwt_data)
    unset_jwt_cookies(response)
    
    return response, 200

@_bp.route('/registro', methods=['POST'])
def registro(usuario_service: Injected[UsuarioService], jwt_token_service: Injected[JwtTokenService]):
    try:
        # Cargar y validar datos de registro
        
        
        # Verificar si el email ya está registrado
        usuario_existente = usuario_service.get_by_email(request.json['email'])
        if usuario_existente:
            return jsonify({"error": "El email ya está registrado"}), 409
        
        # Crear nuevo usuario
        nuevo_usuario = UsuarioModel(
            name=request.json['name'],
            email=request.json['email'],
            password=request.json['password'] 
        )

        # Guardar en la base de datos
        usuario_service.create(nuevo_usuario)
        
        # Crear respuesta con JWT en cookie
        response = jsonify({"mensaje": "Registro exitoso"})

        return response, 201
        
    except Exception as e:
        return jsonify({"error": str(e), "rq":request.json}), 400



