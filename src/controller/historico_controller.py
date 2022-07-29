
from src.controller.IController import IController


class Historico_Controller(IController):
    def store_data(self, data):
        try:
            historico = Historico(data['data'], data['descricao'])
            db.session.add(historico)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def get_data(self):
        return Historico.query.all()
    
    def update_data(self, data):
        try:
            historico = Historico.query.filter_by(id=data['id']).first()
            historico.data = data['data']
            historico.descricao = data['descricao']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def delete_data(self, data):
        try:
            historico = Historico.query.filter_by(id=data['id']).first()
            db.session.delete(historico)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def search_data(self, data):
        return Historico.query.filter_by(id=data['id']).first()