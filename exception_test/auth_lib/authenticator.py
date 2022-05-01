from .user import User
from .auth_exception import *


class Authenticator:

    def __init__(self):
        # Construct an authenticator to manage users logging in and out.
        self.users = {}
        self.administrator = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExit(username)
        if len(password) < 6:
            raise PasswordTooShort(password)
        self.users[username] = User(username, password)

    def add_administrator(self, username, password):
        if username in self.administrator:
            raise UsernameAlreadyExit(username)
        if len(password) < 6:
            raise PasswordTooShort(password)
        self.administrator[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            try:
                user = self.administrator[username]
            except KeyError:
                raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.logged_status = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].logged_status
        elif username in self.administrator:
            return self.administrator[username].logged_status
        else:
            return False


authenticator = Authenticator()
