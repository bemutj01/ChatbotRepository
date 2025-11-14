users=[]

class loginPage:
    @staticmethod
    def checkUserPass(username, password):
        from structure import users
        for u in users:
            if u.username == username and u.password == password:
                return True
        return False

    @staticmethod
    def login():
        from structure import users
        print("\n--- LOGIN PAGE ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if loginPage.checkUserPass(username, password):
            print("Login successful!")
            for u in users:
                if u.username == username:
                    return u
        else:
            print("Incorrect username or password.\n")
            return None

    @staticmethod
    def resetPass():
        from reset import ResetPasswordPage
        return ResetPasswordPage.resetPassword()
    pass

class resetPassPage:
    @staticmethod
    def resetPassword():
        from structure import users
        print("\n--- RESET PASSWORD PAGE ---")

        username = input("Enter your username: ")

        for u in users:
            if u.username == username:
                new_pass = input("Enter your new password: ")
                u.password = new_pass
                print("Password reset successful!\n")
                return True

        print("User not found.\n")
        return False
    pass

class registrationPage:
    @staticmethod
    def register():
        from structure import users, User
        print("\n--- REGISTRATION PAGE ---")

        username = input("Enter new username: ")

        for u in users:
            if u.username == username:
                print("User already exists!\n")
                return False

        password = input("Enter new password: ")

        new_user = User(username, password)
        users.append(new_user)

        print("Registration successful!\n")
        return True
    pass

class employeePage:
    employee = ""
    notify = False
    # TODO: implement employee page.
    pass


class chatPage:
    user = None
    def speak():
        # TODO: implement reading user input
        return
    def respond():
        # TODO: implement chatbot response generation
        return
    def summarize():
        # TODO: implement chat summary generation
        return
    # TODO: implement chat page

    pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chatlogs = []

    def sendChatlog(self, text):
        self.chatlogs.append(text)
    pass

class Chatbot:
    chatlog = []
    def loadchatlog():
        # TODO: receive sendChatlog data
        return
    def respond():
        # TODO: implement chatbot response generation
        return
    def contactEmployee():
        # TODO: implement contact employee functionality
        return
    def read():
        # TODO: implement reading chatlog
        return
    def checkFAQ():
        # TODO: implement FAQ checking functionality
        return
    def summarize():
        # TODO: implement chat summary generation
        return
    #Sends responses to chatPage
    pass

class FAQ:
    frequentlyAskedQuestions = []
    def compareQueryAnswer():
        # TODO: implement query and answer comparison
        return
    def sendAnswers():
        # TODO: implement sending answers to chatbot
        return
    #Stores FAQ data for reuse.
    pass

class Chatlog:
    #information for use loading the chatbot
    text = ""
    identifier = ""
    DateTime = ""
    def __init__(self, text, identifier, DateTime):
        self.text = text
        self.identifier = identifier
        self.DateTime = DateTime
    def setText(self, text):
        self.text = text
        return
    def setIdentifier(self, identifier):
        self.identifier = identifier
        return
    def setDateTime(self, DateTime):
        self.DateTime = DateTime
        return
    def getText(self):
        return self.text
    def getIdentifier(self):
        return self.identifier
    def getDateTime(self):
        return self.DateTime
    
    pass