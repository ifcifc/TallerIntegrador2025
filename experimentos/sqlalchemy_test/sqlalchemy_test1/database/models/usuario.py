from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_empleado = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)

    carritos = relationship("Carrito", back_populates="usuario")

    def __init__(self, nombre, email, password, is_empleado=False, is_delete=False):
        self.nombre = nombre 
        self.email = email
        self.password = password
        self.is_empleado = is_empleado
        self.is_delete = is_delete
