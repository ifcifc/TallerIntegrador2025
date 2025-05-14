from typing import List

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from wireup import Injected, service

from app_core.database import DatabaseService, db
from app_core.models.permission_model import PermissionModel
from app_core.models.usuario_model import UsuarioModel
from app_core.schemas.usuario_model_schema import UsuarioModelSchema


usuario_models_schema = UsuarioModelSchema(many=True)
usuario_model_schema = UsuarioModelSchema()

@service(lifetime="singleton")
class UsuarioService:

    def __init__(self, database_service:Injected[DatabaseService]):
        self.database_service = database_service
        user = UsuarioModel(name="admin", email="admin", password="1234")
        permiso1 = PermissionModel.query.filter_by(name='admin').first()
        user.add_permission(permiso1)
        self.create(user)

    def get_by_id(self,  id:int, return_schema=False)-> UsuarioModel|UsuarioModelSchema|None:
        query = self.database_service.get_session().query(UsuarioModel).filter(UsuarioModel.id == id).first()

        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
        
    def get_by_email(self, email:str, return_schema=False)-> UsuarioModel|UsuarioModelSchema|None:
        query = self.database_service.get_session().query(UsuarioModel).filter(UsuarioModel.email == email).first()
        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query        
        
    def get_by_nick(self, nick:str, return_schema=False)-> UsuarioModel|UsuarioModelSchema|None:
        query = self.database_service.get_session().query(UsuarioModel).filter(UsuarioModel.name == nick).first()
        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
    
    def get_all(self, return_schema=False) -> List[UsuarioModel|UsuarioModelSchema]:
        query = self.database_service.get_session().query(UsuarioModel).all()

        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
    
    def create(self,  usuario:UsuarioModel):
        self.database_service.get_session().add(usuario)
        self.database_service.get_session().commit()

    