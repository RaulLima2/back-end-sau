from flask import Flask,  SQLAlchemy

def init_db() -> SQLAlchemy:
    db = SQLAlchemy()
    return db

def close_db(db: SQLAlchemy) -> SQLAlchemy:
    db.session.close()
    return db

