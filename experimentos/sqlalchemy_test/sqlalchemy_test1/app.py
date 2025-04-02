from database.database import SessionLocal, init_db

init_db()

from database.models.articulo import Articulo

db = SessionLocal()

db.add(Articulo(nombre="Producto 1", precio=10.0))
db.add(Articulo(nombre="Producto 2", precio=20.0))
db.commit()


for producto in db.query(Articulo).all():
    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}")

