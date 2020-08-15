# -*- coding: utf-8 -*-
"""
扩展
"""
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

cors = CORS()
migrate = Migrate()
db = SQLAlchemy()
