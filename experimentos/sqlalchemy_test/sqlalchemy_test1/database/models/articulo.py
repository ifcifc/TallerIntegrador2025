from sqlalchemy import Column, Integer, String, Float
from database.database import Base

class Articulo(Base):
    __tablename__ = 'articulo'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio