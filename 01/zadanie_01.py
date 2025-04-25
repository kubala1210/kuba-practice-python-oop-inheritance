class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_display_name(self):
        return self.name.upper()

    def authorize(self):
        if len(self.password) >= 8:
            return True
        else:
            return False


class Admin(User):

    def has_access(self):
        return True


class Guest(User):

    def authorize(self):
        return False


admin = Admin('Kuba', 'secretpassword')
print(admin.get_display_name())
print(admin.authorize())
print(admin.has_access())

guest = Guest('Anna', 'short')
print(guest.get_display_name())
print(guest.authorize())
