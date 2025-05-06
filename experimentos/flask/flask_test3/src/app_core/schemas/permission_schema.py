from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from app_core.models.permission_model import PermissionModel
from app_core.database import db

class PermissionNameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PermissionModel
        load_instance = True
        include_relationships = False
        include_fk = False
        sqla_session = db.session
        
    # Sólo el nombre del permiso
    name = auto_field(required=True)

