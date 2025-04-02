from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import importlib
import os

DATABASE_URL = "sqlite:///:memory:"
MODELS_PATH = "database/models"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def init_db():
    """
    Inicializa la base de datos y carga los modelos automáticamente."
    """

    #Cargar automaticamente los modelos
    for archivo in os.listdir(MODELS_PATH):
        #Carga todos los archivos .py en la carpeta models
        if archivo.endswith(".py") and archivo != "__init__.py":
            #le saca el .py al nombre del archivo
            nombre_modelo = archivo[:-3]
            #importa el modulo
            modulo = importlib.import_module(f"{MODELS_PATH.replace("/", ".")}.{nombre_modelo}")
            print(f'Modelo {nombre_modelo} cargado: {modulo}')

    # Crear todas las tablas
    Base.metadata.create_all(engine)