'''
User: Represents a user of the app. Attributes: user_id, name, email,
password, payment_info. 
Methods: login, logout, register, edit_profile, delete_account.
'''

class User:
    def __init__(self) -> None:
        self.user_id = 0
        self.name = "bob jones"
        self.email = "benzuke34@gmail.com"
        self.password = "pass"
        self.payment_info = "1234567890"
        self.budget = 0
        self.expenses = []

    '''
    Login to the users account.
    '''
    def login(self):
        pass

    '''
    Logout of the users account.
    '''
    def logout(self):
        pass

    '''
    Register a new user.
    '''
    def register(self):
        pass


    def edit_profile(self):
        pass

    '''
    Delete the users account.
    '''
    def delete_account(self):
        pass
