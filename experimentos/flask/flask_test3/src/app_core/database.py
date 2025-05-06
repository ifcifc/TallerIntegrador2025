from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from wireup import service
from . import wireup_cotainer

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def init(app:Flask):
  db.init_app(app)
  
def create_all(app:Flask):
  with app.app_context():
    db.create_all()

@service(lifetime="singleton")
class DatabaseService():
  def get_db(self):
    return db
  def get_session(self):
    return db.session
  
wireup_cotainer.add_service(DatabaseService)

