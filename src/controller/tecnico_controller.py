from src import db
from model.tecnico import Tecnico
from src.controller.IController import IController


class Tecnico_Controller(IController):
    def store_data(self, data):
        try:
            tecnico = Tecnico(data['nome'], data['descricao'])
            db.session.add(tecnico)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def get_data(self):
        return Tecnico.query.all()

    def update_data(self, data):
        try:
            tecnico = Tecnico.query.filter_by(id=data['id']).first()
            tecnico.nome = data['nome']
            tecnico.descricao = data['descricao']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    
    def delete_data(self, data):
        try:
            tecnico = Tecnico.query.filter_by(id=data['id']).first()
            db.session.delete(tecnico)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def search_data(self, data):
        return Tecnico.query.filter_by(id=data['id']).first()
    
    
         

    