from sqlalchemy import Column, Integer, String
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.database import db

class ApiModel(db.Model):
    __tablename__ = 'apiModel'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)

class ApiModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ApiModel
        load_instance = True
        include_relationships = False  # No incluir relaciones
        include_fk = False  # No incluir claves foráneas
        sqla_session = db.session
    
    # Solo especificamos que name es requerido (como en el modelo original)
    name = auto_field(required=True)