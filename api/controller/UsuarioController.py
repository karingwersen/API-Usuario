from controller.Mongo import Mongo
from model.Usuario import Usuario


class UsuarioController:
    
    @staticmethod
    def alterar_senha_usuario(nova_senha: str, cpf: str):
        mongo = Mongo("usuario")

        resultado = mongo.alterar_senha_usuario(nova_senha, cpf)

        if resultado:
            return True
        else:
            return False
        
    @staticmethod
    def detalhar_usuario(email: str):
        mongo = Mongo("usuario")

        usuario_info = mongo.detalhar_usuario(email)

        if usuario_info is not None:
            usuario_info_json = { 'nome': usuario_info['nome'], 'sobrenome': usuario_info['sobrenome'], 'email': usuario_info['email'], 'cpf': usuario_info['cpf'], 'data_de_nascimento': usuario_info['data_de_nascimento'] }

            return usuario_info_json
        else:
            return None

    @staticmethod
    def criar_usuario(usuario: Usuario):
        mongo = Mongo("usuario")

        resultado = mongo.criar_usuario(usuario)

        if resultado:
            return True

        else:
            return False

    @staticmethod
    def editar_usuario(usuario: Usuario):
        mongo = Mongo("usuario")

        resultado = mongo.editar_usuario(usuario)

        if resultado:
            return True
        else:
            return False

    @staticmethod
    def listar_usuarios():
        mongo = Mongo("usuario")

        usuarios_listados = mongo.listar_usuarios()

        usuarios_retornados = []

        for usuario in usuarios_listados:

            usuario_retornado = { 'nome': usuario["nome"], 'sobrenome': usuario["sobrenome"], 'email': usuario["email"] }

            usuarios_retornados.append(usuario_retornado)

        return usuarios_retornados




