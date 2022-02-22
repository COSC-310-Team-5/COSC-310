from random import randint

class GettingStarted:
    def gettingStarted():
        starterMessages = [] 
        starterMessages.append("How are you feeling?")
        starterMessages.append("What's been bothering you?")
        starterMessages.append("Why would you like to talk?")
        starterMessages.append("What do you feel is wrong?")
        randomMessage = randint(0,3)
        return starterMessages[randomMessage]