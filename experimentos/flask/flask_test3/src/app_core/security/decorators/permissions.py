from functools import wraps
from typing import Set
from types import SimpleNamespace

def api_access(is_public:bool=False, access_permissions:Set[str]=[]):

    def decorator(f):
        # Guardar los metadatos en la función
        f._security_metadata = SimpleNamespace(is_public=is_public, access_permissions=set(access_permissions))
        
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
            
        # Copiar los metadatos a la función decorada
        decorated_function._security_metadata = f._security_metadata
        return decorated_function
        
    return decorator