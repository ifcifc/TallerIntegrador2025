from datetime import datetime, timezone
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Venta(Base):
    __tablename__ = 'venta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    articulo_id = Column(Integer, ForeignKey('articulo.id'), nullable=False)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)

    usuario = relationship('Usuario')
    articulo = relationship('Articulo')

    def __init__(self, usuario_id, articulo_id, precio, cantidad, fecha=None):
        self.fecha = fecha if fecha else datetime.now(timezone.utc)
        self.usuario_id = usuario_id
        self.articulo_id = articulo_id
        self.precio = precio
        self.cantidad = cantidad
