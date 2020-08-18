from {{cookiecutter.app_name}}.extend.helper import BaseModel, Parameter, check_username, check_password


class UserModel(BaseModel):
    username = Parameter(str, check_username)
    password = Parameter(str, check_password)
