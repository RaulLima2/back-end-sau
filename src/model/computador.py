from . import db

class Computador(db.Model):
    __codigo_computador:int = db.Column(db.Integer, primary_key=True, auto_increment=True)
    __modelo:str = db.Column(db.db.String(100), unique=True, nullable=False)
    __patrimonio:str =  db.Column(db.db.String(100), unique=True, nullable=False)
    __fk_codigo_setor:int = db.Column(db.Integer, db.ForeignKey('setor.codigo_setor'), unique=True, nullable=False)
    __fk_codigo_componente:int = db.Column(db.Integer, db.ForeignKey('componentes.codigo_componente'), unique=True, nullable=False)
    setor:str = db.relationship('Setor', unique=True)
    componente:str = db.relationship('Componente', unique=True)


    def get_codigo_computador(self) -> int:
        return self.__codigo_computador
       
    def get_modelo(self) -> str:
        return self.__modelo
    
    def get_patrimonio(self) -> str:
        return self.__patrimonio
    
    def set_modelo(self, modelo) -> bool:
        self.__modelo = modelo

    def set_patrimonio(self, patrimonio) -> bool:
        self.__patrimonio = patrimonio
    
