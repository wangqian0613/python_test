import hashlib


class User:

    def __init__(self, username, password):
        # Create a new user object. The password will be encrypted before storing.
        self.username = username
        self.password = self._encrypted_pw(password)
        self.logged_status = False

    def _encrypted_pw(self, password):
        # Encrypt the password with the username and return the sha digest
        hash_string = (self.username + password)
        hash_string = hash_string.encode('utf-8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        # Return True if the password is valid for this user, false otherwise
        encrypted = self._encrypted_pw(password)
        return encrypted == self.password

