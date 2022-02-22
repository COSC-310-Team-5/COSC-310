#Import all needed classes from the other files
from GreetMessage import GreetMessage
from GoodbyeMessage import GoodbyeMessage
from GettingStarted import GettingStarted
from BotRespons import BotRespons
from DatabaseToList import DatabaseToList

class Main:
    print(GreetMessage.greetMessage())
    userInput = input()
    while(not userInput.replace(' ','').isalpha()):
        print("Please try again, remember to use only letters.")
        userInput = input()
    print(GettingStarted.gettingStarted())
    userWantsToTalk = True
    databaseInList = DatabaseToList.database_to_list()
    while(userWantsToTalk):        
        userInputSentence = input()
        while(not userInputSentence.replace(' ','').isalpha()):
            print("Please try again, remember to use only letters.")
            userInputSentence = input()
        if(len(userInputSentence)<=2):
            print(GoodbyeMessage.goodbyeMessage())
            userWantsToTalk = False
        else:
            botAnswer,correctnessValue = BotRespons.bot_respons(userInputSentence,databaseInList)
            if correctnessValue > 1:
                print("I'm sorry, that seems a little complex for me. Could you say it a little more simply please?")
            elif correctnessValue <= 0:
                print("I'm sorry, I couldn't understand. Could you say that again please?")
            else:
                print(botAnswer)