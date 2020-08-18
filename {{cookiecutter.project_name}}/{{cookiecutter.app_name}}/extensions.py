# -*- coding: utf-8 -*-
"""
扩展
"""
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import func


cors = CORS(supports_credentials=True)
migrate = Migrate()

class BaseModel(Model):
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='修改时间')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


db = SQLAlchemy(model_class=BaseModel)
