from registration import USER_DB  

class ResetPasswordPage:
    @staticmethod
    def reset_password():
        print("\n RESET PASSWORD PAGE ")

        username = input("Enter your username: ")

        if username not in USER_DB:
            print("Error: User does not exist.\n")
            return False

        new_password = input("Enter your new password: ")
        USER_DB[username] = new_password

        print("Password reset successfully!\n")
        return True
