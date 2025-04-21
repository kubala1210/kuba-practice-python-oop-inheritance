class User:
    total_users = 0

    def __init__(self, name):
        self.name = name
        User.total_users += 1

class Admin(User):

    def __init__(self, name):
        super().__init__(name)
        self.role = 'admin'

class Guest(User):

    def __init__(self, name):
        super().__init__(name)
        self.role = 'guest'


# admin = Admin('Anna')
# guest = Guest('Kamil')
# user = User('Adam')
#
# print(User.total_users)
# print(admin.name, admin.role)
# print(guest.name, guest.role)