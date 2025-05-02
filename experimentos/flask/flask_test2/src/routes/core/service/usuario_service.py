from typing import List

from wireup import Injected, service
from core.database import DatabaseService
from routes.core.models.usuario_model import LoginSchema, UsuarioModel, UsuarioModelSchema

usuario_models_schema = UsuarioModelSchema(many=True)
usuario_model_schema = UsuarioModelSchema()

@service(lifetime="singleton")
class UsuarioService:

    def __init__(self, database_service:Injected[DatabaseService]):
        self.database_service = database_service

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
    
    def get_all(self, return_schema=False) -> List[UsuarioModel|UsuarioModelSchema]:
        query = self.database_service.get_session().query(UsuarioModel).all()

        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
    
    def create(self,  usuario:UsuarioModel):
        print(self.database_service.get_session())
        self.database_service.get_session().add(usuario)
        self.database_service.get_session().commit()

    