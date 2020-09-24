from {{cookiecutter.app_name}}.extends.helper import check_username, check_password
from {{cookiecutter.app_name}}.extends.check import BaseModel, Parameter


class UserModel(BaseModel):
    username = Parameter(str, check_username)
    password = Parameter(str, check_password)
