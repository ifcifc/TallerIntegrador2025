from flask_marshmallow import Schema
from sqlalchemy import Column, Integer, String
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from werkzeug.security import generate_password_hash, check_password_hash
from app import database
from marshmallow import Schema, fields, validate, ValidationError

class UsuarioModel(database.db.Model):
    __tablename__ = 'usuarioModel'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    _password = Column(String(128), nullable=False)
    
    @property
    def password(self):
        raise AttributeError('password no es un atributo legible')
    
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self._password, password)
    

class UsuarioModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        load_instance = True
        include_relationships = False  # No incluir relaciones
        include_fk = False  # No incluir claves foráneas
        sqla_session = database.db.session
    
    # Solo especificamos que name es requerido (como en el modelo original)
    name = auto_field(required=True)
    email = auto_field(required=True)

class LoginSchema(Schema):
    email = fields.String(required=True, validate=validate.Length(min=1))
    password = fields.String(required=True, validate=validate.Length(min=1))