from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(close_db)
    with app.app_context():
        db.create_all()

def close_db(e=None):
    pass # flask-sqlalchemy handles closing the session automatically.

# from .models import student