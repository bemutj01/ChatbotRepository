from structure import User, users
class resetPassPage:
    @staticmethod
    def resetPassword():
        print("\n RESET PASSWORD PAGE ")

        username = input("Enter your username: ")

        for u in users:
            if u.username == username:
                newPass = input("Enter your new password: ")
                u.password = newPass
                print("Password reset successful!\n")
                return True

        print("User not found.\n")
        return False
    pass

def main():
    resetPassPage.resetPassword()

if __name__ == "__main__":
    main()
