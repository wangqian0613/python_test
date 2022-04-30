class AuthException(Exception):

    def __init__(self, username, user=None):
        super(AuthException, self).__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExit(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionsError(AuthException):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass

