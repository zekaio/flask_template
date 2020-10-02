import typing


class Result:
    status = None
    _msg = None
    _data = None

    @classmethod
    def data(cls, _data: typing.Union[dict, str]):
        cls._data = _data
        return cls

    @classmethod
    def msg(cls, _msg: typing.Union[dict, str]):
        cls._msg = _msg
        return cls
    
    @classmethod
    def build(cls):
        return {
            'status': cls.status,
            'msg': cls._msg,
            'data': cls._data
        }

    @classmethod
    def OK(cls):
        cls.status = 200
        cls._msg = 'OK'
        return cls