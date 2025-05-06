from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from sqlalchemy import Column, Connection, ForeignKey, Integer, String, Table, insert,event
from app_core.database import db
from sqlalchemy.orm import relationship

usuario_permiso = Table(
    'usuario_permiso',
    db.Model.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarioModel.id'), primary_key=True),
    Column('permiso_id', Integer, ForeignKey('permissionModel.id'), primary_key=True)
)

class PermissionModel(db.Model):
    __tablename__ = 'permissionModel'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    usuarios = relationship(
        'UsuarioModel',
        secondary=usuario_permiso,
        back_populates='permisos'
    )


# Define la función que se ejecutará después de crear la tabla
@event.listens_for(PermissionModel.__table__, 'after_create')
def insert_default_values(target, connection:Connection, **kw):
    db.session.add(PermissionModel(name="admin"))
    db.session.add(PermissionModel(name="root.index"))
    db.session.commit()
    