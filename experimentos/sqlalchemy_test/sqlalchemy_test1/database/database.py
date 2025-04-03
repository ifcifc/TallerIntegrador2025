from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import importlib
import os

DATABASE_URL = "sqlite:///:memory:"
MODELS_PATH = "database/models"
IMPORT_PATH = MODELS_PATH.replace('/', '.')

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def init_db():
    """
    Inicializa la base de datos y carga los modelos automáticamente."
    """

    # Verificar si el directorio MODELS_PATH existe
    if not os.path.isdir(MODELS_PATH):
        raise FileNotFoundError(f"El directorio '{MODELS_PATH}' no existe.")

    # Cargar automaticamente los modelos
    for archivo in os.listdir(MODELS_PATH):
        #Carga todos los archivos .py en la carpeta models
        if archivo.endswith(".py") and archivo != "__init__.py":
            #le saca el .py al nombre del archivo
            nombre_modelo = archivo[:-3]
            try: 
                #importa el modulo
                importlib.import_module(f"{IMPORT_PATH}.{nombre_modelo}")
                print(f'Modelo {nombre_modelo} cargado correctamente.')
            except ImportError as e:
                # Agregar "from e" para mantener la traza de la excepción original
                raise ImportError(f'Error al cargar el modelo {nombre_modelo}: {e}') from e

    # Crear todas las tablas
    Base.metadata.create_all(engine)