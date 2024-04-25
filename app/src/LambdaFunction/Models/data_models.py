from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer,primary_key=True, autoincrement="auto")
    nome = Column(String(100))
    senha = Column(String(100))
    email = Column(String(100))

    funcao_id = Column(Integer, ForeignKey('funcao.id'))
    turno_id = Column(Integer, ForeignKey('turno.id'))



class Funcao(Base):
    __tablename__ = 'funcao'

    id = Column(Integer,primary_key=True, autoincrement='auto')
    nome_funcao = Column(String(100))


class Turno(Base):
    __tablename__ = 'turno'

    id = Column(Integer,primary_key=True, autoincrement="auto")
    nome = Column(String(100))