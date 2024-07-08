from sqlalchemy import create_engine, String, Column, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class Prueba(base):
    __tablename__ = "prueba"
    id = Column(INTEGER ,primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(20))

