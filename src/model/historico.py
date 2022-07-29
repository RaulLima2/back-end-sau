from . import db
from datetime import date, datetime

class Historico(db.Model):
    __tablename__ = 'historico'
    __codigo_historico:int = db.Column(db.Integer, primary_key=True, auto_increment=True)
    __data_atualizacao:date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    __descricao_servico:str = db.Column(db.String(300), nullable=False)
    __grau_importancia:str = db.Column(db.String(100), nullable=False)

    
    #getters
    def get_codigo_historico(self):
        return self.__codigo_historico

    def get_data_atualizacao(self):
        return self.__data_atualizacao
    
    def get_descricao_servico(self):
        return self.__descricao_servico
    
    def get_grau_importancia(self):
        return self.__grau_importancia

    #setters
    def set_codigo_historico(self, codigo_historico:str):
        self.__codigo_historico = codigo_historico

    def set_data_atualizacao(self, data_atualizacao:date):
        self.__data_atualizacao = data_atualizacao

    def set_descricao_servico(self, descricao_servico:str):
        self.__descricao_servico = descricao_servico

    def set_grau_importancia(self, grau_importancia:str):
        self.__grau_importancia = grau_importancia
    
