from ...src import db
from model.componenetes import Componentes
from src.controller.IController import IController


class Componentes_Controller(IController):
    def store_data(self, data):
        try:
            componentes = Componentes(data['nome'], data['descricao'])
            db.session.add(componentes)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def get_data(self):
        return Componentes.query.all()

    def update_data(self, data):
        try:
            componentes = Componentes.query.filter_by(id=data['id']).first()
            componentes.nome = data['nome']
            componentes.descricao = data['descricao']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def delete_data(self, data):
        try:
            componentes = Componentes.query.filter_by(id=data['id']).first()
            db.session.delete(componentes)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def search_data(self, data):
        return Componentes.query.filter_by(id=data['id']).first()
    
    def trigger_data(self):
        pass
    
    def view():
        pass

    def function():
        pass