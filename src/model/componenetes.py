from . import db


class Componentes(db.Model):
    __tablename__ = 'componentes'
    __codigo_componente:int = db.Column(db.Integer, primary_key=True, auto_increment=True, unique=True, nullable=False)
    __tipo_componente:str = db.Column(db.String(100), unique=True, nullable=False)
    __valor:float = db.Column(db.Float, unique=True, nullable=False)

    def __init__(self, tipo_componente, valor):
        self.__tipo_componente = tipo_componente
        self.__valor = valor

    def get_tipo_componente(self):
        return self.__tipo_componente
    
    def get_valor(self):
        return self.__valor
    
    def set_tipo_componente(self, tipo_componente):
        self.__tipo_componente = tipo_componente
    
    def set_valor(self, valor):
        self.__valor = valor