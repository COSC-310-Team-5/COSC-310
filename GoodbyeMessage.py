from random import randint

class GoodbyeMessage:
    def goodbyeMessage():
        goodbyeMessages = []
        goodbyeMessages.append("Have a good day.")
        goodbyeMessages.append("See you next time.")
        goodbyeMessages.append("Bye bye.")
        goodbyeMessages.append("Until next time.")
        randomMessage = randint(0,3)
        return goodbyeMessages[randomMessage]