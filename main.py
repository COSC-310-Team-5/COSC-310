#Import all needed classes from the other files
from GreetMessage import GreetMessage
from GoodbyeMessage import GoodbyeMessage
from GettingStarted import GettingStarted
from BotRespons import BotRespons
from DatabaseToList import DatabaseToList

class Main:
    print(f"Bot: {GreetMessage.greetMessage()}")
    userInput = input("User: ")
    while((not userInput.replace(' ','').isalpha()) or (len(userInput.split()) == (not 1)) ):
        print("Please try again, remember to use only letters.")
        userInput = input("User: ")
    print(f"Bot: {GettingStarted.gettingStarted()}")
    userWantsToTalk = True
    databaseInList = DatabaseToList.database_to_list()
    while(userWantsToTalk):        
        userInputSentence = input("User: ")
        while((not userInputSentence.replace(' ','').isalpha()) or (len(userInputSentence) == 0) ):
            print("Please try again, remember to use only letters.")
            userInputSentence = input("User: ")
        if(len(userInputSentence.split())<=2):
            print(f"Bot: {GoodbyeMessage.goodbyeMessage()}")
            userWantsToTalk = False
        else:
            botAnswer,correctnessValue = BotRespons.bot_respons(userInputSentence,databaseInList)
            if correctnessValue > 1 or correctnessValue <= (1/3):
                print("Bot: I'm sorry, that seems a little complex for me. Could you say it a little more simply please?")
            else:
                print(f"Bot: {botAnswer}")
            correctnessValue = 0