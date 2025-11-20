from structure import users
class LoginService:

    def login(self):
        print("\n LOGIN PAGE ")

        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self._check_credentials(username, password)

        if user:
            print("Login successful!")
            return user
        else:
            print("Incorrect username or password.\n")
            return None

    def _check_credentials(self, username, password):
        for u in users:
            if u.username == username and u.password == password:
                return u
        return None

def main():
    service = LoginService()
    user = service.login()
    if user:
        print("Welcome,", user.username)

if __name__ == "__main__":
    main()
