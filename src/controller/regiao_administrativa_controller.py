from ...src import db
from src.controller.IController import IController
from model.regiao_administrativa import Regiao_Administrativa


class IRegiao_administrativa(IController):
    def store_data(self, data):
        try:
            regiao_administrativa = regiao_administrativa(data['nome'], data['descricao'])
            db.session.add(regiao_administrativa)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def get_data(self):
        return Regiao_Administrativa.query.all()
    
    def update_data(self, data):
        try:
            regiao_administrativa = Regiao_Administrativa.query.filter_by(id=data['id']).first()
            regiao_administrativa.nome = data['nome']
            regiao_administrativa.descricao = data['descricao']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
        
    def delete_data(self, data):
        try:
            regiao_administrativa = Regiao_Administrativa.query.filter_by(id=data['id']).first()
            db.session.delete(Regiao_Administrativa)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
        
    def search_data(self, data):
        return Regiao_Administrativa.query.filter_by(id=data['id']).first()