'''
User: Represents a user of the app. Attributes: user_id, name, email,
password, payment_info. 
Methods: login, logout, register, edit_profile, delete_account.
'''

class User:
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.password = ""
        self.budget = 0
        self.expenses = []