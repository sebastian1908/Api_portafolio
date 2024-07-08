from sqlalchemy import create_engine, String, Column, INTEGER, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class RecuperarPass(base):
    __tablename__ = "recuperar_pass"
    ID = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    CODIGO = Column(INTEGER, nullable=False)
    ID_USUARIO = Column(INTEGER, nullable=True)
    ACTIVO = Column(INTEGER, default=1)
    FECHA_CREACION = Column(DateTime, default=func.now(), nullable=False)
    

