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

# Columna
__Representa una columna en la tabla de la db__

| Argumento            | Tipo/Valores               | Descripción                                                                 | Ejemplo                                      | Obligatorio |
|----------------------|----------------------------|-----------------------------------------------------------------------------|----------------------------------------------|-------------|
| **Tipo de dato**     | `Integer`, `String`, etc.  | Tipo de dato de la columna (primer argumento posicional)                   | `Column(Integer)`                           | Sí          |
| `primary_key`        | `bool`                     | Si es clave primaria                                                       | `primary_key=True`                          | No          |
| `ForeignKey`         | `ForeignKey("tabla.col")`  | Define relación con otra tabla                                             | `ForeignKey("users.id")`                    | No          |
| `nullable`           | `bool` (default: `True`)   | Permite valores NULL                                                       | `nullable=False`                            | No          |
| `default`            | Valor/función              | Valor por defecto (Python)                                                 | `default=0`                                 | No          |
| `server_default`     | `text("SQL")`              | Valor por defecto (SQL)                                                    | `server_default=text("NOW()")`              | No          |
| `unique`             | `bool`                     | Valores únicos                                                             | `unique=True`                               | No          |
| `index`              | `bool`                     | Crea índice para optimización                                              | `index=True`                                | No          |
| `name`               | `str`                      | Nombre en BD (si difiere del atributo)                                     | `name="user_name"`                          | No          |
| `autoincrement`      | `bool`/`'auto'`            | Auto-incremento para PKs                                                   | `autoincrement=True`                        | No          |
| `onupdate`           | Valor/función              | Valor al actualizar                                                        | `onupdate=datetime.now`                     | No          |


```py
    from sqlalchemy import Column
    Column(
        nombre_columna,        # Opcional nombre de la columna en la db
        tipo_de_dato,          # Obligatorio (primer argumento posicional)
        ForeignKey(...),       # Opcional (si es clave foránea)
        otros_argumentos       # Resto de parámetros como keyword arguments
    )
```

# Principales Tipos de Datos en SQLAlchemy

| Tipo de dato               | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `Integer`                  | Enteros (ej: 1, -5, 1000)                                                  |
| `String(length)`           | Cadena de texto con longitud máxima                                        |
| `Text`                     | Texto largo para contenido extenso                                         |
| `Boolean`                  | Valor booleano (True/False)                                                |
| `DateTime`                 | Fecha y hora (almacena datetime de Python)                                 |
| `Date`                     | Solo fecha (sin hora)                                                      |
| `Time`                     | Solo hora (sin fecha)                                                      |
| `Float`                    | Números decimales de precisión simple                                      |
| `Numeric(precision, scale)`| Números decimales con precisión controlada                                 |
| `JSON`                     | Almacena datos en formato JSON                                             |
| `Enum(*values)`            | Lista de valores permitidos                                                |
| `LargeBinary`              | Datos binarios (imágenes, archivos)                                        |
| `UUID`                     | Identificadores únicos universales                                         |
| `Interval`                 | Períodos de tiempo (diferencia entre fechas)                               |
| `BIGINT`                   | Enteros de gran tamaño (mayor rango que Integer)                           |
| `Unicode(length)`          | Similar a String pero para texto Unicode                                   |
| `UnicodeText`              | Similar a Text pero para texto Unicode                                     |
| `PickleType`               | Almacena objetos Python serializados                                       |
| `Interval`                 | Períodos de tiempo                                                        |
| `CHAR(length)`             | Cadena de longitud fija                                                    |
