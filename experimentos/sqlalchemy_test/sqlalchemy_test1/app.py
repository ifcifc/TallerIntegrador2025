from database.database import SessionLocal, init_db
from database.models.articulo import Articulo
from database.models.carrito import Carrito
from database.models.usuario import Usuario

init_db()

db = SessionLocal()

db.add(Articulo(nombre="Producto 1", precio=10.0))
db.add(Articulo(nombre="Producto 2", precio=20.0))

db.add(Usuario(nombre="Usuario 1", email="2@w.com", password="123"))

db.add(Carrito(articulo_id=1, usuario_id=1, cantidad=3))

db.commit()


for producto in db.query(Articulo).all():
    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}")


for carrito in db.query(Carrito).all():
    articulo = carrito.articulo
    print(f"Carrito ID: {carrito.id}, Articulo: {articulo.nombre}, Precio: {articulo.precio}, Cantidad: {carrito.cantidad}")