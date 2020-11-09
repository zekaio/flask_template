"""
扩展
"""
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query, Session

cors = CORS(supports_credentials=True)
migrate = Migrate()


class _SQLAlchemy(SQLAlchemy):
    session: Session


db = _SQLAlchemy()


class Model(db.Model):
    __abstract__ = True

    query: Query

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def _update(self, _except: list = None, alias: dict = None, **kwargs):
        _except = _except or []
        alias = alias or {}
        for key, value in kwargs.items():
            key = alias.get(key) or key
            if key not in _except:
                if hasattr(self, key):
                    setattr(self, key, value)
