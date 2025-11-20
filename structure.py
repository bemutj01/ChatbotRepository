<<<<<<< Updated upstream
=======
users = []

>>>>>>> Stashed changes
class loginPage:
    def checkUserPass(username, password):
        # TODO: implement user/pass verification
        return False; 
    def login(username, password): 
        # TODO: implement page jump to chatPage if verified
        return 
    
    def resetPass(username):
        # TODO: implement page jump to resetPassPage
        return
    # TODO: implement login page
    pass

class resetPassPage:
<<<<<<< Updated upstream
    def resetPassword(username, newPassword):
        # TODO: implement password reset functionality
        return
    # TODO: implement reset password page
=======
    @staticmethod
    def resetPassword():
        print("\n RESET PASSWORD PAGE ")

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
        # Lazy import to avoid circular top-level imports
        from registration import register as _register
        return _register(users, User)
>>>>>>> Stashed changes
    pass

class employeePage:
    #Employee page representation with contact info property
    def __init__(self, employee="", notify=False, userPhoneNumber="", userEmail=""):
        self.employee = employee
        self.notify = notify
        self.userPhoneNumber = userPhoneNumber
        self.userEmail = userEmail
        self._userContactInfo = [self.userPhoneNumber, self.userEmail]

    @property
    def userContactInfo(self):
        #Return [phone, email] for the employee.
        return list(self._userContactInfo)

    @userContactInfo.setter
    def userContactInfo(self, value):
        #Set the contact info; expects a list/tuple of two items: [phone, email]. This also updates `userPhoneNumber` and `userEmail` fields.
        if not isinstance(value, (list, tuple)) or len(value) != 2:
            raise ValueError("userContactInfo must be a list or tuple [phone, email]")
        self._userContactInfo = [value[0], value[1]]
        self.userPhoneNumber, self.userEmail = self._userContactInfo


<<<<<<< Updated upstream
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

=======
>>>>>>> Stashed changes

class User:
    username = ""
    password = ""
    chatlogs = []
    def sendChatlog():
        # TODO: implement chatlog send to chatbot
        return
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
    #FAQ storage and lookup using a 2D list of [question, answer].
    def __init__(self, faqs=None):
        # Expect faqs to be an iterable of [question, answer] pairs.
        self.faqs = [list(pair) for pair in faqs] if faqs else []

    def compareQueryAnswer(self, query):
        #Return the index of a question that matches `query`, or -1 if none.
        if not isinstance(query, str):
            return -1
        q_norm = query.strip().lower()
        for i, pair in enumerate(self.faqs):
            if not pair:
                continue
            stored_q = pair[0]
            if isinstance(stored_q, str) and stored_q.strip().lower() == q_norm:
                return i
        return -1

    def sendAnswer(self, query):
        #Return the answer corresponding to `query`, or `None` if not found.
        idx = self.compareQueryAnswer(query)
        if idx != -1:
            return self.faqs[idx][1]
        return None

    def add_faq(self, question, answer):
       #Add a question/answer pair to the FAQ store.
        self.faqs.append([question, answer])

class Chatlog:
    text = ""
    identifier = ""
    DateTime = ""
    #information for use loading the chatbot
    pass