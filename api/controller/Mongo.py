from pymongo import MongoClient
from model.Usuario import Usuario


class Mongo:

    def __init__(self):
        self.conexao = None
        self.client = None

    def __init__(self,dbname : str):
        self.criar_conexao(dbname=dbname)

    def criar_client(self):
        self.client = MongoClient()

    def criar_conexao(self, dbname: str):

        self.criar_client()

        self.conexao = getattr(self.client, dbname)

    def fechar_conexao(self):
        self.client.close()

    def alterar_senha_usuario(self, nova_senha: str, cpf: str):
        try:
            collection = getattr(self.conexao, "usuario")

            filter = { 'cpf': cpf }

            new_value = { "$set": { 'senha': nova_senha } }

            collection.update_one(filter, new_value)

            return True

        except:
            return False
        
    def detalhar_usuario(self, email: str):
        try:
            collection = getattr(self.conexao, "usuario")

            filter = { 'email': email }

            usuario = collection.find_one(filter)

            return usuario

        except:
            return None

    def criar_usuario(self, usuario:Usuario):
        try:
            collection = getattr(self.conexao, "usuario")

            usuario_a_ser_criado = { 'nome': usuario.nome, 'sobrenome': usuario.sobrenome, 'email': usuario.email, 'senha': usuario.senha, 'data_de_nascimento': usuario.data_de_nascimento, 'cpf': usuario.cpf }

            collection.insert_one(usuario_a_ser_criado)

            return True

        except:
            return False

    def editar_usuario(self, usuario: Usuario):
        try:
            collection = getattr(self.conexao, "usuario")

            filter = { 'cpf': usuario.cpf }

            new_value =  { "$set": { 'nome' : usuario.nome, 'sobrenome': usuario.sobrenome, 'email': usuario.email, 'data_de_nascimento': usuario.data_de_nascimento, 'cpf': usuario.cpf } }

            collection.update_one(filter, new_value)

            return True

        except:
            return False

    def listar_usuarios(self):
        try:
            collection = getattr(self.conexao, "usuario")

            usuarios = collection.find()

            return usuarios

        except:
            return None




