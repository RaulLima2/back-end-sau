from . import db

class Usuario(db.Model):
        __tablename__ = 'usuario'
        __id:int = db.Column(db.Integer, primary_key=True, auto_inclement=True)
        __nome:str = db.Column(db.String(100), nullable=False)
        __email:str = db.Column(db.String(100), unique=True, nullable=False)
        __cpf:str = db.Column(db.String(100), unique=True, nullable=False)
        __fk_codigo_setor:int = db.Column(db.Integet, db.ForeignKey(
            'Setor.codigo_setor', 
            _constraint='fk_codigo_setor', 
            ondelete='cascade', 
            onupdate='cascade'
            ),
            nullable=False
        )
        __setor = db.relationship('Setor', unique=True)


        def get_id(self) -> int:
            return self.__id
        
        def get_nome(self) -> str:
            return self.__nome
        
        def get_email(self) -> str:
            return self.__email
        
        def get_cpf(self) -> str:
            return self.__cpf
        
        def get_codigo_setor(self) -> int:
            return self.__fk_codigo_setor
        
        def get_setor(self) -> Setor:
            return self.__setor

        def set_id(self, id) -> bool:
            self.__id = id
        
        def set_nome(self, nome) -> bool:
            self.__nome = nome

        def set_email(self, email) -> bool:
            self.__email = email

        def set_cpf(self, cpf) -> bool:
            self.__cpf = cpf
        
        def set_setor(self, setor) -> bool:
            self.__setor = setor