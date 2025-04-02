from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Carrito(Base):
    __tablename__ = 'carrito'

    id = Column(Integer, primary_key=True, autoincrement=True)
    articulo_id = Column(Integer, ForeignKey('articulo.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    is_closed = Column(Boolean, default=False)

    # Relaciones opcionales (si quieres acceder a los objetos relacionados)
    #articulo = relationship("Articulo", back_populates="carritos")
    #usuario = relationship("Usuario", back_populates="carritos")

    def __init__(self, articulo_id, usuario_id, cantidad=1, is_closed=False):
        self.articulo_id = articulo_id
        self.usuario_id = usuario_id
        self.cantidad = cantidad
        self.is_closed = is_closed