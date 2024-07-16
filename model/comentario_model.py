from sqlalchemy import create_engine, String, Column, INTEGER, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class Comentarios(base):
    __tablename__ = "comentarios"
    ID = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    COMENTARIO = Column(String(30), nullable=True)
    ID_NOTICIA = Column(INTEGER, nullable=False)
    ID_USUARIO = Column(INTEGER, nullable=False)
    ACTIVO = Column(INTEGER, default=1)
    FECHA_CREACION = Column(DateTime, default=func.now(), nullable=False)
    

