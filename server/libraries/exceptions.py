"""Define custom exceptions"""


class ValidationError(Exception):
    """Custom exception 422"""

    def __init__(self, message, code=422, data=None):
        self.message = message
        self.code = code
        self.data = data

    def __str__(self):
        return repr({
            'message': self.message,
            'code': self.code,
            'data': self.data
        })
