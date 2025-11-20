def register(users, User):
    print("\n REGISTRATION PAGE ")

    username = input("Enter new username: ")

    for u in users:
        if getattr(u, "username", None) == username:
            msg = "User already exists!"
            print(msg + "\n")
            return [["status", "error"], ["message", msg], ["username", username]]

    password = input("Enter new password: ")

    new_user = User(username, password)
    users.append(new_user)

    msg = "Registration successful!"
    print(msg + "\n")
    return [["status", "success"], ["message", msg], ["username", username]]


if __name__ == "__main__":
    # If run directly, import structure and call register using its users/User.
    import structure
    register(structure.users, structure.User)