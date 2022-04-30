import auth_lib
import sys
print(sys.path)

auth_lib.authenticator.add_user('joe', 'joe_password')
auth_lib.authorizer.add_permission('test_program')
auth_lib.authorizer.add_permission('change_program')
auth_lib.authorizer.permit_user('test_program', 'joe')





