from numbers import Number
from typing import List
from sqlalchemy import Column, Integer, String, select
from werkzeug.security import generate_password_hash, check_password_hash
from app_core.database import db
from sqlalchemy.orm import relationship
from .permission_model import PermissionModel, usuario_permiso

class UsuarioModel(db.Model):
    __tablename__ = 'usuarioModel'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    _password = Column(String(128), nullable=False)

    # Relación muchos a muchos con permisos
    permisos = relationship(
        'PermissionModel',
        secondary=usuario_permiso,
        back_populates='usuarios'
    )

    @property
    def password(self):
        raise AttributeError('password no es un atributo legible')
    
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def add_permission(self, id_permission:Number|List[Number]):
        if isinstance(id_permission, list):
            self.permisos.extends(id_permission)
        else:
            self.permisos.append(id_permission)

    def get_permissions(self):
        return [permiso.name for permiso in self.permisos]