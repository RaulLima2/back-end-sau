from ...src import db

class Tecnico(db.Model):
    __tablename__ = 'tecnico'
    __id =  db.Column(db.Integer, primary_key=True, auto_increment=True)
    __nome = db.Column(db.String(100), nullable=False)
    __email = db.Column(db.String(100), unique=True, nullable=False)
    __cargo = db.Column(db.String(100), nullable=False)
    __codigo_setor = db.Column(db.String(100), nullable=False)

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_cargo(self):
        return self.__cargo

    def get_codigo_setor(self):
        return self.__codigo_setor

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_codigo_setor(self, codigo_setor):
        self.__codigo_setor = codigo_setor