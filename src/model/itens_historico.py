from . import db
from .usuario import Usuario
from .tecnico import Tecnico
from .setor import Setor
from .historico import Historico
from .computador import Computador


class itens_historico(db.Model):
    __tablename__ = 'itens_historico'
    __codigo_historico: str = db.Column(
        db.db.Integer,
        primary_key=True,
        auto_inclement=True
    )
    __fk_codigo_setor: str = db.Column(
        db.Integer,
        db.ForeignKey(
            'setor.codigo_setor',
            _constraint='fk_codigo_setor',
            ondelete='cascade',
            onupdate='cascade'
        ),
        nullable=False
    )
    __fk_codigo_computador: str = db.Column(
        db.db.Integer,
        db.ForeignKey(
            'computador.codigo_computador',
            _constraint='fk_codigo_computador',
            ondelete='cascade',
            onupdate='cascade'
        )
    )
    __fk_codigo_usuario: str = db.Column(
        db.Integer,
        db.ForeignKey(
            'usuario.codigo_usuario',
            _constraint='fk_codigo_usuario',
            ondelete='cascade',
            onupdate='cascade'
        ),
        nullable=False
    )
    __fk_codigo_tecnico: str = db.Column(
        db.Integer,
        db.ForeignKey(
            'tecnico.codigo_tecnico',
            _constraint='fk_codigo_tecnico',
            ondelete='cascade',
            onupdate='cascade'
        ),
        nullable=False
    )

    setor: Setor = db.relationship('Setor', unique=True)
    tecnico: Tecnico = db.relationship('Tecnico', unique=True)
    usuario: Usuario = db.relationship('Usuario', unique=True)
    computador: Computador = db.relationship('Computador', unique=True)
    historico: Historico = db.relationship('Historico', unique=True)

    def set_codigo_item_historico(self, codigo_item_historico) -> bool:
        self.__codigo_item_historico = codigo_item_historico

    def get_codigo_item_historico(self) -> str:
        return self.__codigo_item_historico

    def get_codigo_setor(self) -> str:
        return self.__fk_codigo_setor

    def get_codigo_computador(self) -> str:
        return self.__fk_codigo_computador

    def get_codigo_usuario(self) -> str:
        return self.__fk_codigo_usuario

    def get_codigo_tecnico(self) -> str:
        return self.__fk_codigo_tecnico
