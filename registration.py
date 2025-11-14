USER_DB = {}   
class RegistrationPage:
    @staticmethod
    def register():
        print("\n USER REGISTRATION PAGE ")

        username = input("Enter email/username: ")

        # Check existing users
        if username in USER_DB:
            print("Error: User already exists.\n")
            return False

        password = input("Enter password: ")

        # Create user
        USER_DB[username] = password

        print("Registration successful! \n")
        return True