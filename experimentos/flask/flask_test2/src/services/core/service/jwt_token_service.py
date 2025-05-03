import datetime
from flask import jsonify
from flask_jwt_extended import create_access_token, decode_token
from cachetools import TTLCache
import jwt
from wireup import service
from core.app_core import jwt, app

#Cache de tokens JWT para evitar que accedan a los servicion con un token revocado
#Tambien podria usarse para almacenar algunos metadatos del token para evitar la sobrecarga del token y la DB
_jwt_token_cache = TTLCache(maxsize=20000, ttl=app.config["JWT_ACCESS_TOKEN_EXPIRES"])

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    return not jti in _jwt_token_cache

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    response = jsonify({"msg": "Token ha expirado, elimina la cookie"})
    response.set_cookie("access_token_cookie", "", expires=0) 
    return response, 401

@service
class JwtTokenService:
    def __init__(self):
        pass

    def create_access_token(self, id_usuario:int, perms=[], **kwargs):
        token = create_access_token(**kwargs)
        decoded_token = decode_token(token)
        jti = decoded_token["jti"]
        _jwt_token_cache[jti] = {
            "create_at": datetime.datetime.now(),
            "id_usuario": id_usuario,
            "perms": perms
        }
        
        return token
    
    def revoke_token(self, token):
        jti = token["jti"]
        if jti in _jwt_token_cache:
            del _jwt_token_cache[jti]
    
    def is_valid_token(self, token):
        return token["jti"] in _jwt_token_cache
    
    def get_token_meta(self, token):
        jti = token["jti"]
        if jti in _jwt_token_cache:
            return _jwt_token_cache[jti]
        return None
    
    def get_tokens_by_user(self, id_usuario:int)-> tuple:
        tokens = []
        for jti, token in _jwt_token_cache.items():
            if token["id_usuario"] == id_usuario:
                tokens.append({
                    "jti": jti,
                    "meta": token
                })
        return tuple(tokens)