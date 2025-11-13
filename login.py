from registration import USER_DB   

class LoginPage:
    @staticmethod
    def login():
        print("\n LOGIN PAGE ")

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username not in USER_DB:
            print("Error: User does not exist.\n")
            return False

        if USER_DB[username] != password:
            print("Error: Incorrect password.\n")
            return False

        print("Login successful!\n")
        return True



