'''
    Menu Layout 
     
    Developed by Jordan and Trent

    Purpose: A simple menu layout our AVL

'''

# Import packages
from packages import *

# Declare Global Variables
dashLine = "-"
numOfLines = 50
lineBarrier = dashLine * numOfLines 

# Shows menu to user
def menu():
    # Declare Variables 
    userInput = ""
    errorFlag = False


    # ===== Original wordTree with preset words =====
    wordTree = AVL_Tree("Car")
    wordTree.insert("Football")
    wordTree.insert("Apple")
    wordTree.insert("Ladder")
    wordTree.insert("Family")
    wordTree.insert("Bagel")
    wordTree.insert("Motorcycle")
    wordTree.insert("Dog")

    # Print header for start up
    print(lineBarrier)
    print("Welcome, user!")

    # Start Loop to keep user in menu
    while True:
        # Print menu header
        print(lineBarrier)
        print("AVL Word Look Up Menu")
        print(lineBarrier)

        # Print menu options
        print("1. Insert a Word")
        print("2. Search for a Word")
        print("3. Delete a Word")
        print("Q. Quit")
        print(lineBarrier)

        # If there was an error previously (Wrong Input) show message
        if (errorFlag):  
            # Special Case: If input is just enter, clear error. It returns to screen anyways
            if userInput == "":
                errorFlag = False       
            
            # Otherwise, show error
            else:
                print(f"Sorry, {userInput} is not an option!")
                print(lineBarrier)

        print("Please Select an Option Above")
        print(lineBarrier)

        # Get user input
        userInput = input("").capitalize()


        '''
            Switch Statement
            Based on Input go to function, and reset errorFlag
            If input DOES NOT match any cases, raise errorFlag

            Menu Options

            1. Insert
            2. Search
            3. Delete
            Q. Quit

            NOTE: Parameters (wordTree[AVL Tree Object], lineBarrier)

        '''


        match userInput:
            case "1":
                # Clear Terminal
                terminalCleaner()
                errorFlag = False
                insertWord(wordTree, lineBarrier)
            case "2":
                # Clear Terminal
                terminalCleaner()
                errorFlag = False
                searchWord(wordTree, lineBarrier)
            case "3":
                # Clear Terminal
                terminalCleaner()
                errorFlag = False
                deleteWord(wordTree, lineBarrier)
            case "Q":
                print(dashLine * numOfLines)
                terminalCleaner()
                print("Goodbye!")
                print(dashLine * numOfLines)
                print("Final AVL Tree (in-order with height):")
                print(dashLine * numOfLines)
                inorder_with_true_height(wordTree.root)
                break
            case _:
                errorFlag = True
                terminalCleaner()
                

def main():
    # Run following functions
    terminalCleaner()
    menu()


if __name__ == '__main__':
    main()