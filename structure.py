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
    def resetPassword(username, newPassword):
        # TODO: implement password reset functionality
        return
    # TODO: implement reset password page
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
    text = ""
    identifier = ""
    DateTime = ""
    #information for use loading the chatbot
    pass