# Import Modules
from ..clearterminal import *

def insertWord(lineBarrier):

    # Declare Variables 
    userInput = ""
    foundWord = ""
    wordInsertedFlag = False
    errorFlag = False

    '''
        NOTE:   We need to have a search in this function to search for duplicate words
                If found, Alert User
    
    '''

    # Start Loop to keep user in menu
    while userInput != "B":
        # Print Header
        print(lineBarrier)
        print("Insert a Word")
        print(lineBarrier)
        print("Press B to go back to Menu")
        print(lineBarrier)

        # If there was an error previously (Wrong Input OR Word in AVL) show message
        if (errorFlag):
            if (userInput == foundWord):
                print(f"Sorry, {userInput} already in list!")
            else:
                print("Sorry, Enter a Word!")
            print(lineBarrier)

        # If insert went successfully show message
        if (wordInsertedFlag):
            print(f"Inserted {userInput} to dictonary!")
            print(lineBarrier)
        


        # Get user input
        # Title if two words, ice cream -> Ice Cream
        userInput = input().title()

        # Place holder for search function
        foundWord = "Test"

        # If userInput is not in AVL and not empty append it to dictonary
        if ((userInput != foundWord) and (userInput != "")):
            print(lineBarrier)
            errorFlag = False
            wordInsertedFlag = True
        # Otherwise raise error
        else:
            errorFlag = True
            wordInsertedFlag = False
        
        # Clear terminal in loop
        terminalCleaner()

    # Clear terminal if user returns
    terminalCleaner()