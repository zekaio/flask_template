# -*- coding: utf-8 -*-
from {{cookiecutter.app_name}}.extend.helper import HttpError
from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.models.database import *


def get_user(**kwargs) -> User:
    user: User = (
        User
        .query
        .filter_by(**kwargs)
        .first()
    )
    
    return user