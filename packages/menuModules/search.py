# Import Modules
from ..clearterminal import *

def searchWord(lineBarrier):

    # Declare Variables 
    userInput = ""
    foundWord = ""
    foundWordFlag = False
    errorFlag = False

    
    '''
        TODO:   Link search to function
    '''

    # Start Loop to keep user in menu
    while userInput != "B":
        # Print Header
        print(lineBarrier)
        print("Search a Word")
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

        # If search went successfully show message
        if (foundWordFlag):
            print(f"{userInput} found in AVL!")
            print(lineBarrier)


        # Get user input
        userInput = input().title()

        # Place holder for search function
        foundWord = "Test"

        # Check to see if word was found
        if (userInput == foundWord):
            foundWordFlag = True
            errorFlag = False
        # Otherwise prompt error
        else:
            foundWordFlag = False
            errorFlag = True
        
        # Clear terminal in loop
        terminalCleaner()

    # Clear terminal if user returns
    terminalCleaner()