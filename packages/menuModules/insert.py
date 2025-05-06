# Import Modules
from ..clearterminal import *
from ..node import *

def insertWord(wordTree:AVL_Tree, lineBarrier):

    # Declare Variables 
    userInput = ""
    errorMessage = ""
    wordInsertedFlag = False
    errorFlag = False

    # Start Loop to keep user in menu
    while userInput != "B":
        # Print Header
        print(lineBarrier)
        print("Insert a Word".center(50))
        print(lineBarrier)
        print("B. To go back to Menu")
        print(lineBarrier)

        # If there was an error previously (Wrong Input OR Word in AVL) show message
        if (errorFlag):
            print(errorMessage)
            print(lineBarrier)

        # If insert went successfully show message
        if (wordInsertedFlag):
            print(f"Inserted {userInput} to tree!")
            print(lineBarrier)
        

        # Get user input
        # Title if two words, ice cream -> Ice Cream
        userInput = input().title().lstrip()

        # Check to see if input is return (B)
        if (userInput == "B"):
            # If so, break out of loop
            break
        # Otherwise, continue with insert
        else:
            
            # Call Node file to insert into tree
            errorMessage, errorFlag = wordTree.insert(userInput)

            # If there is no error message and errorFlag returned false from Node File 
            # show message to user on next loop!
            if ((errorMessage == "") and (errorFlag == False)):
                print(lineBarrier)
                errorFlag = False
                wordInsertedFlag = True
            # Otherwise show error
            else:
                wordInsertedFlag = False
            
            # Clear terminal in loop
            terminalCleaner()

    # Clear terminal if user returns
    terminalCleaner()