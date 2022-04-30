from .auth_exception import *
from .authenticator import *


class Authorizer:

    def __init__(self, authenticators):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        # Create a new permission that users can be added to
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionsError('Permission Exists')

    def permit_user(self, perm_name, username):
        # Grant the given permission to the user
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionsError('Permission does not Exists')
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionsError('Permission does not Exists')
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


authorizer = Authorizer(authenticator)
