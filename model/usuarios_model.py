from sqlalchemy import create_engine, String, Column, INTEGER, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class Usuarios(base):
    __tablename__ = "usuarios"
    ID = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    NOMBRE = Column(String(20), nullable=True)
    APELLIDO = Column(String(20), nullable=True)
    ACTIVO = Column(INTEGER, default=1)
    USUARIO = Column(String(20), nullable=False)
    PASS = Column(String(20), nullable=False)
    FECHA_CREACION = Column(DateTime, default=func.now(), nullable=False)
    

