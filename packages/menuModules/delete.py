# Import Modules
from ..clearterminal import *

def deleteWord(lineBarrier):
    # Declare Variables 
    userInput = ""
    foundWord = ""
    wordDeletedFlag = False
    errorFlag = False

    '''
        TODO:   Link search to function
    '''

    # Start Loop to keep user in menu
    while userInput != "B":
        # Print Header
        print(lineBarrier)
        print("Delete a Word")
        print(lineBarrier)
        print("Press B to go back to Menu")
        print(lineBarrier)

        # If there was an error previously (Wrong Input OR Word in NOT AVL) show message
        if (errorFlag):
            if (userInput == ""):
                print("Sorry, Enter a Word!")
            else:
                print(f"{userInput} not in AVL!")
            
            print(lineBarrier)

        # If delete went successfully show message
        if (wordDeletedFlag):
            print(f"{userInput} deleted from AVL!")
            print(lineBarrier)
        


        # Get user input
        userInput = input().title()

        # Place holder for search function
        foundWord = "Test"

        # If userInput is in AVL and not empty delete from AVL
        if ((userInput == foundWord) and (userInput != "")):
            print(lineBarrier)
            errorFlag = False
            wordDeletedFlag = True
        # Otherwise raise error
        else:
            errorFlag = True
            wordDeletedFlag = False
        
        # Clear terminal in loop
        terminalCleaner()

    # Clear terminal if user returns
    terminalCleaner()