# Import Modules
from ..clearterminal import *
from ..node import *

def deleteWord(wordTree:AVL_Tree, lineBarrier):
    # Declare Variables 
    userInput = ""
    deletedWord = ""
    resultMessage = ""
    wordDeletedFlag = False
    canceledFlag = False
    errorFlag = False

    # Start Loop to keep user in menu
    while userInput != "B":
        # Print Header
        print(lineBarrier)
        print("Delete a Word".center(50))
        print(lineBarrier)
        print("Press B to go back to Menu")
        print(lineBarrier)

        # If there was an error previously (Wrong Input OR Word in NOT AVL) show message
        if (errorFlag):
            if ((userInput == "") or (userInput.isnumeric())):
                print("Sorry, Enter a Word!")
            else:
                print(resultMessage)
            
            print(lineBarrier)

        # If deletion was canceled show message
        if ((not wordDeletedFlag) and (canceledFlag) and (userInput != "")):
            print(f"Deletion Canceled!")
            print(lineBarrier)

        # If delete went successfully show message
        if ((wordDeletedFlag) and (not canceledFlag)):
            print(f"{deletedWord} deleted from AVL!")
            deletedWord = ""
            print(lineBarrier)
        


        # Get user input
        userInput = input().title().lstrip()

        # Call Node file to search into tree
        foundword, resultMessage = wordTree.search(userInput)

        # If word was found in AVL and input is not a number 
        # give user a warning for deletion
        if ((foundword != None) and (userInput.isnumeric() == False)):
            while True:
                # Clear terminal for deletion prompt
                terminalCleaner()

                # Show warning message for deletion
                print(lineBarrier)
                print("Warning!".center(50))
                print(lineBarrier)
                print(f"You are about to delete {foundword.val}.")
                print("Would you like to continue? (yes/no)")
                print(lineBarrier)
                
                # Get user input
                userInput = input().title().lstrip()

                # If user inputted yes, 
                # set wordDeletedFlag to True and canceledFlag to False
                # ALSO Call Node file to remove node
                if (userInput == "Yes"):
                    deletedWord = foundword.val
                    wordDeletedFlag = True
                    canceledFlag = False
                    wordTree.delete(deletedWord)
                    break
                # Otherwise, set canceledFlag to True
                else:
                    wordDeletedFlag = False
                    canceledFlag = True
                    break
                
            errorFlag = False
        
        # Otherwise raise error
        else:
            errorFlag = True
            wordDeletedFlag = False
            canceledFlag = False
        
        # Clear terminal in loop
        terminalCleaner()

    # Clear terminal if user returns
    terminalCleaner()