from sqlalchemy import create_engine, String, Column, INTEGER, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class Noticias(base):
    __tablename__ = "noticia"
    ID = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    TITULO = Column(String(30), nullable=False)
    DESCRIPCION = Column(String(500), nullable=False)
    ACTIVO = Column(INTEGER, default=1)
    FECHA_CREACION = Column(DateTime, default=func.now(), nullable=False)
    

