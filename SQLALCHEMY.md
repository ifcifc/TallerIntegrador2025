# Conexion
__Establece la conexion con la base de datos__
* Argumento __echo__ activa o desactiva los logs de sqlalchemy en la consola

```py
    from sqlalchemy import create_engine

    engine = create_engine(CONNECTION_STRING, echo=False)
```

# Sesion
__sessionmaker crea una clase que servira para interactual con la base de datos__

* Argumento __bind__ indica el motor de la base de datos que se va a usar
* Argumento __autoflush__ indica si sqlalchemy actualize los cambios automaticamente a la base de datos.
* Argumento __autocommit__ indica si se haran los commits automaticamente en la trasacciones o no 

__`db = SessionLocal()` crea la sesion a usar para manipular la base de datos__

```py
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    db = SessionLocal()
```

# Creacion de modelos

__El metodo `declarative_base()` crea un modelo base del cual deberan heredar los demas modelos__


```py
    from sqlalchemy import declarative_base

    Base = declarative_base()

    class Modelo(Base):
        __tablename__ = 'modelo'

        id = Column(Integer, primary_key=True, autoincrement=True)
        is_deleted = Column(Boolean, default=False)

    # Crear todas las tablas
    Base.metadata.create_all(engine)
```