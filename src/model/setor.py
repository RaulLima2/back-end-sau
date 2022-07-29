from . import db

class Setor(db.Model):
    __codigo_setor: str = db.Column(db.String(100), primary_key=True)
    __nome: str = db.Column(db.String(100))
    __descricao: str = db.Column(db.db.String(100))
    __fk_codigo_ra: str = db.Column(
        db.String(100),
        db.ForeignKey(
            'regiao_administrativa.codigo_ra',
            __constraint='fk_codigo_ra',
            ondelete='cascade',
            onupdate='cascade'
        ),
        nullable=False
    )
    ra = db.relationship('regiao_administrativa', unique=True)


    def get_nome(self) -> str:
        return self.__nome

    def get_numero_funcionarios(self) -> str:
        return self.__numero_funcionarios

    def get_descricao(self):
        return self.__descricao

    def get_codigo_ra(self):
        return self.__fk_codigo_ra

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_numero_funcionarios(self, numero_funcionarios: str):
        self.__numero_funcionarios = numero_funcionarios

    def set_descricao(self, descricao: str):
        self.__descricao = descricao
