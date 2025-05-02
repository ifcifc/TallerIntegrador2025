import importlib
import pkgutil
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
#import models

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def init(app:Flask):
  db.init_app(app)

  #pkgutil.iter_modules obtiene los modulos en el paquete models
  #for _, module_name, _ in pkgutil.iter_modules(models.__path__):
      #Cargo el modelo
      #importlib.import_module(f"models.{module_name}")
  
def create_all(app:Flask):
  with app.app_context():
    db.create_all()