from random import random

class GreetMessage:
    def greetMessage():
        greetMessages = []
        greetMessages.append("Hello.")
        greetMessages.append("How do you do?")
        greetMessages.append("Hi!")
        greetMessages.append("Good day.")
        randomMessage = round(random()*5)
        return greetMessages[randomMessage]