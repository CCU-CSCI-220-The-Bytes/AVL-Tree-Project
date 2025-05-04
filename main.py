'''
    Menu Layout by Trent

    Purpose: A simple menu layout our AVL
    Notes: Not official, wanted an outline 

'''

'''
    NOTE: For testing I set the word "Test" for all functions

    Insert => "Sorry, Test already in list!" 
    Insert => "Test, found in AVL!" <= Possibly call class function for output and show what level it's at.
    Insert => "Test deleted from AVL"

'''

# Import packages
from packages import *

# Declare Global Variables
dashLine = "-"
numOfLines = 35
lineBarrier = dashLine * numOfLines 

# Shows menu to user
def menu():
    # Declare Variables 
    userInput = ""
    errorFlag = False

    # Print header for start up
    print(lineBarrier)
    print("Welcome, user!")

    # Start Loop to keep user in menu
    while userInput != "Q":
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
            If input DOES NOT match cases, raise errorFlag

            Menu Options

            1. Insert
            2. Search
            3. Delete

            NOTE: Parameters (Class object [Node], lineBarrier)

        '''


        match userInput:
            case "1":
                # Clear Terminal
                terminalCleaner()
                errorFlag = False
                insertWord(lineBarrier)
            case "2":
                # Clear Terminal
                terminalCleaner()
                errorFlag = False
                searchWord(lineBarrier)
            case "3":
                # Clear Terminal
                terminalCleaner()
                errorFlag = False
                deleteWord(lineBarrier)
            case "Q":
                print(dashLine * numOfLines)
                print("Goodbye!")
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