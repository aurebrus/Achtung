class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExitsError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass

class UserAlredyRegError(UserError):
    pass

class InvalidEmailError(UserError):
    pass

