from {{cookiecutter.app_name}}.extensions import db, Model

class User(Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
