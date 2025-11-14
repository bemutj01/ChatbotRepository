from structure import loginPage

def run_login():
    user = loginPage.login()
    if user:
        print(f"Welcome {user.username}!")

if __name__ == "__main__":
    run_login()
