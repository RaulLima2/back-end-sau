from src import db
from model.setor import Setor
from src.controller.IController import IController


class Setor_Controller(IController):
    def store_data(self, data):
        try:
            setor = Setor(data['nome'], data['descricao'])
            db.session.add(setor)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def get_data(self):
        return Setor.query.all()
    
    def update_data(self, data):
        try:
            setor = Setor.query.filter_by(id=data['id']).first()
            setor.nome = data['nome']
            setor.descricao = data['descricao']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def delete_data(self, data):
        try:
            setor = Setor.query.filter_by(id=data['id']).first()
            db.session.delete(setor)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def search_data(self, data):
        return Setor.query.filter_by(id=data['id']).first()

    