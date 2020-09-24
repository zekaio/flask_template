class HttpError(Exception):
    def __init__(self, message, status_code):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            'errcode': self.status_code,
            'errmsg': self.message
        }
