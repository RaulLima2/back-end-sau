from . import db


class regiao_administrativa(db.Model):
    __tablename__ = 'regiao_administrativa'
    __codigo_ra: int = db.Column(
        db.Integer,
        primary_key=True,
        auto_inclement=True
    )
    __local: str = db.Column(db.String(100), unique=True, nullable=False)

    def get_codigo_ra(self) -> str:
        return self.__codigo_ra
    
    def get_local(self) -> str:
        return self.__local
    
    def set_codigo_ra(self, codigo_ra:str) -> bool:
        self.__codigo_ra = codigo_ra

    def set_local(self, local:str) -> bool:
        self.__local = local
        