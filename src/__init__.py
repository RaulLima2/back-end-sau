from .db import init_db
from .app import create_app
from flask import Flask, SQLAlchemy

db:SQLAlchemy = init_db()
app:Flask = create_app(db)