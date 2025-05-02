from typing import List
from routes.core.models.usuario_model import LoginSchema, UsuarioModel, UsuarioModelSchema
from database import db

usuario_models_schema = UsuarioModelSchema(many=True)
usuario_model_schema = UsuarioModelSchema()

class UsuarioService:
    def get_by_id(id:int, return_schema=False)-> UsuarioModel|UsuarioModelSchema|None:
        query = db.session.query(UsuarioModel).filter(UsuarioModel.id == id).first()

        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
        
    def get_by_email(email:str, return_schema=False)-> UsuarioModel|UsuarioModelSchema|None:
        query = db.session.query(UsuarioModel).filter(UsuarioModel.email == email).first()

        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
    
    def get_all(return_schema=False) -> List[UsuarioModel|UsuarioModelSchema]:
        query = db.session.query(UsuarioModel).all()

        if return_schema:
            return usuario_models_schema.dump(query)
        else:
            return query
    
    def create(usuario:UsuarioModel):
        db.session.add(usuario)
        db.session.commit()

    