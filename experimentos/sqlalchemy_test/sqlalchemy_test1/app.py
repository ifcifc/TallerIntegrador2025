from database.database import SessionLocal, init_db
from database.models.articulo import Articulo
from database.models.carrito import Carrito
from database.models.usuario import Usuario
from database.models.venta import Venta
from sqlalchemy import and_, or_

init_db()

db = SessionLocal()

db.add(Articulo(nombre="Producto 1", precio=10.0))
db.add(Articulo(nombre="Producto 2", precio=20.0))

for I in range(100):
    db.add(Articulo(nombre=f"Producto {I}", precio=I*10))

db.add(Usuario(nombre="Usuario 1", email="2@w.com", password="123"))

db.add(Carrito(articulo_id=1, usuario_id=1, cantidad=3))
db.add(Carrito(articulo_id=2, usuario_id=1, cantidad=43))

db.add(Venta(articulo_id=1, usuario_id=1, cantidad=3, precio=10.0))

db.commit()


for producto in db.query(Articulo).all():
    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}")

print("--------------------------------------------")
for carrito in db.query(Carrito).all():
    articulo = carrito.articulo
    usuario = carrito.usuario
    print(f"Usuario ID: {usuario.id}, Nombre: {usuario.nombre}")
    print(f"Carrito ID: {carrito.id}, Articulo: {articulo.nombre}, Precio: {articulo.precio}, Cantidad: {carrito.cantidad}")


print("--------------------------------------------")
usuario = db.query(Usuario).filter(Usuario.id == 1).first()
carritos = usuario.carritos
for c in carritos:
    articulo = c.articulo
    print(f"Carrito ID: {c.id}, Articulo: {articulo.nombre}, Precio: {articulo.precio}, Cantidad: {c.cantidad}")
  
print("--------------------------------------------")
for venta in db.query(Venta).all():
    articulo = venta.articulo
    usuario = venta.usuario
    print(f"Usuario ID: {usuario.id}, Nombre: {usuario.nombre}")
    print(f"Venta ID: {venta.id}, Articulo: {articulo.nombre}, Precio: {venta.precio}, Cantidad: {venta.cantidad}")


print("--------------------------------------------")

# (precio>900 and precio<980) or (precio % 66 == 0)
filtros = or_(
    and_(Articulo.precio > 900, Articulo.precio<980),
    Articulo.precio % 66 == 0,
)
ls = db.query(Articulo).filter(filtros).all()

for producto in ls:
    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}")