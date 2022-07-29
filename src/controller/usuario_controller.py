from ...src import db
from sqlalchemy import DDL 
from model.usuario import Usuario
from IController import IController

class UsuarioController(IController):
    def store_data(self, data):
        try:
            usuario = usuario(data['nome'], data['login'], data['senha'])
            db.session.add(usuario)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def get_data(self):
        return Usuario.query.all()
    
    def update_data(self, data):
        try:
            usuario = Usuario.query.filter_by(id=data['id']).first()
            usuario.nome = data['nome']
            usuario.login = data['login']
            usuario.senha = data['senha']
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def delete_data(self, data):
        try:
            usuario = Usuario.query.filter_by(id=data['id']).first()
            db.session.delete(usuario)
            db.session.commit()
        except:
            db.rollback()
            raise
        finally:
            db.session.close()

    def search_data(self, data):
        return Usuario.query.filter_by(id=data['id']).first()
    
    def view_attendente(self):
        try:
            view:DDL = DDL(
                "CREATE VIEW IF NOT EXISTS view_attendente AS "
                "SELECT FROM WHERE"
            )
            db.session.execute(view)
        except:
            db.rollback()
            raise
        finally:
            db.session.close()
    
    def trigger_attendente(self):
        try:
            trigger:DDL = DDL(
                "CREATE TRIGGER IF NOT EXISTS trigger_attendente AFTER INSERT ON  FOR EACH ROW "
                "BEGIN "
                "   INSERT INTO usuario (nome, login, senha) VALUES (NEW.nome, NEW.login, NEW.senha); "
                "END"
            )
            db.session.execute(trigger)
        except:
            db.rollback()
            raise
        finally:
            db.session.close()