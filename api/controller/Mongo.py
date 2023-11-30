from pymongo import MongoClient

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







