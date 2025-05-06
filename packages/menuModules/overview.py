# Import Modules
from ..clearterminal import *
from ..node import *

def overview(wordTree:AVL_Tree, lineBarrier):
    # Declare Variables 
    userInput = ""
    errorFlag = False

    # Start Loop to keep user in menu
    while userInput != "B": 
        print(lineBarrier)
        print("Overview".center(50))
        print(lineBarrier)
        print("Current AVL Tree (in-order with height):")
        print(lineBarrier)
        inorder_with_true_height(wordTree.root)
        print(lineBarrier)
        print("B. To go back to Menu")
        print(lineBarrier)

        # If there was an error previously (Wrong Input) show message
        if (errorFlag):
            # If input is blank reset errorFlag (It will remain on the same screen)
            if (userInput == ""):
                errorFlag = False
            else:
                print(f"Sorry, {userInput} is not an option!")
                print(lineBarrier)

        # Get user input
        userInput = input().title().lstrip()

        # If input is not B, set errorFlag to true 
        # and on next loop show message
        if (userInput != "B"):
            errorFlag = True

        # Clear terminal in loop
        terminalCleaner()
    
    # Clear terminal if user returns
    terminalCleaner()
