import typing


def check_username(username: str) -> typing.Union[bool, typing.Tuple[bool, str]]:
    if (username_len := len(username)) < 6 or username_len > 12:
        return False, '用户名必须是6到12个字符'
    return True


def check_password(password: str) -> typing.Union[bool, typing.Tuple[bool, str]]:
    if len(password) < 6:
        return False, '密码必须大于6位'
    return True
