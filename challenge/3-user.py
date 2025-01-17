class User:
    def __init__(self):
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if value is None or isinstance(value, str):
            self._password = value
        else:
            self._password = None

    def is_valid_password(self, pwd):
        if not isinstance(pwd, str):
            return False
        return self._password == pwd


if __name__ == "__main__":
    user_1 = User()
    user_1.password = "MyPwd"
    u_pwd = user_1.password
    if u_pwd is None:
        print("User.password should not be None after set")

    user_2 = User()
    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")
