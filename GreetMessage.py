from random import randint

class GreetMessage:
    def greetMessage():
        greetMessages = []
        greetMessages.append("Hello.")
        greetMessages.append("How do you do?")
        greetMessages.append("Hi!")
        greetMessages.append("Good day.")
        randomMessage = randint(0,3)
        return greetMessages[randomMessage]