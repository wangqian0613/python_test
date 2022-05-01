import auth_lib
import sys

# auth_lib.authenticator.add_user('joe', 'password')
# auth_lib.authenticator.add_administrator('wang', 'password')
# auth_lib.authorizer.add_permission('test_program')
# auth_lib.authorizer.add_permission('change_program')
# auth_lib.authorizer.permit_user('test_program', 'wang')
# auth_lib.authorizer.permit_user('change_program', 'wang')
# auth_lib.authorizer.permit_user('change_program', 'joe')


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            'add_permission': self.add_permission,
            'permit_for_admin': self.permit_for_admin,
            'sign': self.sign,
            'login': self.login,
            'test': self.test,
            'change': self.change,
            'quit': self.quit

        }

    def add_permission(self):
        perm_name = input('perm_name: ')
        auth_lib.authorizer.add_permission(perm_name)

    def permit_for_admin(self):
        admin_name = input('admin_name: ')
        perm_name = input('perm_name: ')
        auth_lib.authorizer.permit_user(perm_name, admin_name)

    def sign(self):
        username = input('username: ')
        password = input('password: ')
        right_type = input('right_type: ')
        if right_type == 'user':
            auth_lib.authenticator.add_user(username, password)
        elif right_type == 'admin':
            auth_lib.authenticator.add_administrator(username, password)
        else:
            print("right_type is error")

    def login(self):
        logged_in = False
        while not logged_in:
            username = input('username: ')
            password = input('password: ')
            try:
                logged_in = auth_lib.authenticator.login(username, password)
            except auth_lib.InvalidUsername:
                print('Sorry, that username does not exist')
                break
            except auth_lib.InvalidPassword:
                print('Sorry, incorrect password')
            else:
                self.username = username
                print('Login success!')

    def is_permitted(self, permission):
        try:
            auth_lib.authorizer.check_permission(permission, self.username)
        except auth_lib.NotLoggedInError:
            print('Sorry, {} is not logged in'.format(self.username))
            return False
        except auth_lib.NotPermittedError:
            print('Sorry, {} can not {}'.format(self.username, permission))
            return False
        except auth_lib.PermissionsError:
            print('Sorry, system has not {}'.format(permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted('test_program'):
            print('Testing program now...')

    def change(self):
        if self.is_permitted('change_program'):
            print('Changing program now...')

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ''
            while True:
                print(
                    '''
                    Please enter a command:
                    \tadd_permission\tAddPermission
                    \tpermit_for_admin\tPermitForAdmin
                    \tsign\tSign
                    \tlogin\tLogin
                    \ttest\tTest the program
                    \tchange\tChange the program
                    \tquit\tQuit 
                    '''
                )
                answer = input('Enter a command: ').lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print('{} is not a valid option'.format(answer))
                else:
                    func()
        finally:
            print('Thank you for testing the auth module')


Editor().menu()



