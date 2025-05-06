# Import Modules
from ..clearterminal import *
from ..node import *

def searchWord(wordTree:AVL_Tree, lineBarrier):

    # Declare Variables 
    userInput = ""
    resultMessage = ""
    foundWordFlag = False
    errorFlag = False

    # Start Loop to keep user in menu
    while userInput != "B":
        # Print Header
        print(lineBarrier)
        print("Search a Word")
        print(lineBarrier)
        print("B. To go back to Menu")
        print(lineBarrier)

        # If there was an error previously (Wrong Input OR Word in NOT AVL) show message
        if (errorFlag):
            if ((userInput == "") or (userInput.isnumeric())):
                print("Sorry, Enter a Word!")
            else:
                print(resultMessage)
            
            print(lineBarrier)

        # If search went successfully show message
        if (foundWordFlag):
            print(resultMessage)
            print(lineBarrier)

        # Get user input
        userInput = input().title().lstrip()

        # Call Node file to search into tree
        foundword, resultMessage = wordTree.search(userInput)

        # If word was found in AVL and input is not a number 
        # show results on next loop
        if ((foundword != None) and (userInput.isnumeric() == False)):
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