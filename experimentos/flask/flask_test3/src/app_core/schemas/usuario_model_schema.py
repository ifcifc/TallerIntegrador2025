from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields

from app_core.models.usuario_model import UsuarioModel
from app_core.database import db
from app_core.schemas.permission_schema import PermissionNameSchema


class UsuarioModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        load_instance = True
        include_relationships = True   # Incluir relaciones
        include_fk = False
        exclude = ('_password',)
        sqla_session = db.session

    # Campos básicos
    name  = auto_field(required=True)
    email = auto_field(required=True)
    
    # Campo personalizado que convierte la lista de objetos permisos en lista de nombres
    permisos = fields.Method("get_permisos_names")
    
    def get_permisos_names(self, obj):
        # Extrae solo los nombres de los permisos y los retorna como una lista
        return [permiso.name for permiso in obj.permisos]