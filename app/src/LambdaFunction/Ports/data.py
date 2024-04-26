import sqlalchemy as db
from Models import data_models
from sqlalchemy.orm import sessionmaker
from aws_lambda_powertools import Logger
from Ports import parameter_store


stringConexao = parameter_store.get_parameter("connectionDbString")

engine = db.create_engine(stringConexao)

Session = sessionmaker(bind=engine)

session = Session()

logger = Logger()

def cadastrar_usuario(usuario: data_models.Usuario):
    try:
        logger.info(f"Adicionando usuario: {usuario.email}")
        session.add(usuario)
        session.commit()
        logger.info("Usuario adicionado")
    except Exception as err:
        logger.exception(f"Erro ao adicionar usuario: {usuario.email}")
        raise err
    finally:
        session.close()