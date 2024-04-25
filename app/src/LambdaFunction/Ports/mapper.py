from Models import data_models


def mapear_usuario(usuario) -> data_models.Usuario:
    usuario_model = data_models.Usuario()
    usuario_model.email = usuario['email']
    usuario_model.nome = usuario['nome']
    usuario_model.funcao_id = usuario['funcao']
    usuario_model.turno_id = usuario['turno']
    usuario_model.senha = 'teste1'

    return usuario_model