from ...src import db
from model.computador import Computador
from src.controller.IController import IController


class Computador_Controller(IController):
    def store_data(self, data):
        try:
            computador = Computador(data['nome'], data['descricao'])
            db.session.add(computador)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def get_data(self):
        return Computador.query.all()

    def update_data(self, data):
        try:
            computador = Computador.query.filter_by(id=data['id']).first()
            computador.nome = data['nome']
            computador.descricao = data['descricao']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def delete_data(self, data):
        try:
            computador = Computador.query.filter_by(id=data['id']).first()
            db.session.delete(computador)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def search_data(self, data):
        return Computador.query.filter_by(id=data['id']).first()