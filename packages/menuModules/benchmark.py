# Import Modules
from ..clearterminal import *
from ..node import *
import time as t 

def benchmark(lineBarrier):
    # Declare Constants
    filePath = "packages/data/wordFile.txt"
    
    # Declare Variables 
    userInput = ""

    # Try-Except: For wordFile
    try:
       
        def createObjectsWithFirstWord():
            # Open file
            wordFile = open(filePath)

            # If found place first word into AVL and Dictonary
            firstWord = wordFile.readline()

            # AVL Tree
            wordTreeTest = AVL_Tree(firstWord)

            # Dictionary
            pythonDictonaryTest = {0: firstWord}

            # Close file
            wordFile.close()

            # Return objects
            return wordTreeTest, pythonDictonaryTest

        # Function to choose test
        def testPicker(nameOfTest, testingObj, numLinesToRead, findWord):
            # Insert first word into both objects
            # AVL_TREE() reqiures a root node to start off of. 
            wordTreeTest, pythonDictonaryTest = createObjectsWithFirstWord()

            if (nameOfTest == "insert"):
                if (testingObj == "AVL"):
                    return insertTest(wordTreeTest, numLinesToRead)
                else:
                    return insertTest(pythonDictonaryTest, numLinesToRead)
            
            elif (nameOfTest == "search"):
                if (testingObj == "AVL"):
                    return searchTest(wordTreeTest, numLinesToRead, findWord)
                else:
                    return searchTest(pythonDictonaryTest, numLinesToRead, findWord)
                
            elif (nameOfTest == "delete"):
                if (testingObj == "AVL"):
                    return deleteTest(wordTreeTest, numLinesToRead, findWord)
                else:
                    return deleteTest(pythonDictonaryTest, numLinesToRead, findWord)
            else:
                print(f"ERR: {nameOfTest}, {testingObj}, {numLinesToRead}, {findWord} doesn't match!")

        



        # Function for Insert Test
        def insertTest(item, numLines):
            # Open wordFile
            with open(filePath) as fileContents:
                # Check to see if variable (item) is either AVL or Dictionary
                if (isinstance(item, AVL_Tree)):
                    # Start time and go to loop
                    startTime = t.perf_counter()
                    for i, line in enumerate(fileContents):
                        # Since we got the first word already we don't insert again 
                        if i == 0:
                            continue
                        # If line number reaches to input break out of loop
                        elif i >= numLines:
                            break
                        # Otherwise, insert to item
                        else:
                            item.insert(line.strip())                        
                            
                    # End Time
                    endTime = t.perf_counter()

                    # Go to function to get total time spent inserting 
                    return calculateTotalTime(startTime, endTime)

                elif (isinstance(item, dict)):
                   # Start time and go to loop
                    startTime = t.perf_counter()
                    for i, line in enumerate(fileContents):
                        # Since we got the first word already we don't insert again 
                        if i == 0:
                            continue
                        # If line number reaches to input break out of loop
                        elif i >= numLines:
                            break
                        # Otherwise, append to item
                        else:
                            item[i] = line.strip()

                            
                    # End Time
                    endTime = t.perf_counter()

                    # Go to function to get total time spent inserting 
                    return calculateTotalTime(startTime, endTime)

        # Function to search
        def searchTest(item, numLines, findWord):
            # Open wordFile
            with open(filePath) as fileContents:
                # Check to see if variable (item) is either AVL or Dictionary
                if (isinstance(item, AVL_Tree)):
                    # Go though loop to populate object
                    for i, line in enumerate(fileContents):
                        # Since we got the first word already we don't insert again 
                        if i == 0:
                            continue
                        # If line number reaches to input break out of loop
                        elif i >= numLines:
                            break
                        # Otherwise, insert to item
                        else:
                            item.insert(line.strip())                        
                    
                    # Start time
                    startTime = t.perf_counter()

                    # Go thorugh AVL
                    item.search(findWord)                    

                    # End Time
                    endTime = t.perf_counter()

                    # Go to function to get total time spent searching 
                    return calculateTotalTime(startTime, endTime)

                elif (isinstance(item, dict)):
                    # Go though loop to populate object
                    for i, line in enumerate(fileContents):
                        # Since we got the first word already we don't insert again 
                        if i == 0:
                            continue
                        # If line number reaches to input break out of loop
                        elif i >= numLines:
                            break
                        # Otherwise, append to item
                        else:
                            item[i] = line.strip()                  
                    # Start time
                    startTime = t.perf_counter()
                    
                    # Go through dictonary 
                    for value in item.values():
                        if value == findWord:
                            break

                    # End Time
                    endTime = t.perf_counter()

                    # Go to function to get total time spent searching 
                    return calculateTotalTime(startTime, endTime)
                

        # Function to delete
        def deleteTest(item, numLines, findWord):
            # Open wordFile
            with open(filePath) as fileContents:
                # Check to see if variable (item) is either AVL or Dictionary
                if (isinstance(item, AVL_Tree)):
                    # Go though loop to populate object
                    for i, line in enumerate(fileContents):
                        # Since we got the first word already we don't insert again 
                        if i == 0:
                            continue
                        # If line number reaches to input break out of loop
                        elif i >= numLines:
                            break
                        # Otherwise, insert to item
                        else:
                            item.insert(line.strip())                        
                    
                    # Start time
                    startTime = t.perf_counter()

                    # Go thorugh AVL
                    item.delete(findWord)                    

                    # End Time
                    endTime = t.perf_counter()

                    # Go to function to get total time spent deleting 
                    return calculateTotalTime(startTime, endTime)

                elif (isinstance(item, dict)):
                    # Go though loop to populate object
                    for i, line in enumerate(fileContents):
                        # Since we got the first word already we don't insert again 
                        if i == 0:
                            continue
                        # If line number reaches to input break out of loop
                        elif i >= numLines:
                            break
                        # Otherwise, append to item
                        else:
                            item[i] = line.strip()                  
                    # Start time
                    startTime = t.perf_counter()
                    
                    # Go through dictonary 
                    for key, value in item.items():
                        if value == findWord:
                            del item[key]
                            break

                    # End Time
                    endTime = t.perf_counter()

                    # Go to function to get total time spent deleting 
                    return calculateTotalTime(startTime, endTime)

        # Function to calculate total time
        def calculateTotalTime(sTime, fTime):
            totalTime = fTime - sTime
            return round(totalTime, 4)
        

        # Start Loop to keep user in menu
        while userInput != "B":
    
            # Print header
            print(lineBarrier)
            print("Benchmark".center(50))
            print(lineBarrier)

            print("Benchmark creates a new tree for testing purposes.")
            print(lineBarrier)
            print("Press any key except B to run the test again")
            print("B. To go back to Menu")
            print(lineBarrier)

            print("INSERT".center(50))
            print(lineBarrier)

            # INSERT TESTS
            
            # 50 WORDS
            print("Insertion of 50 words")
            print(f"AVL Time: {testPicker("insert", "AVL", 50, None)} seconds")
            print(f"Dictonary Time: {testPicker("insert", "DIC", 50, None)} seconds\n")

            # 100 WORDS
            print("Insertion of 100 words")
            print(f"AVL Time: {testPicker("insert", "AVL", 100, None)} seconds")
            print(f"Dictonary Time: {testPicker("insert", "DIC", 100, None)} seconds\n")

            # 500 WORDS
            print("Insertion of 500 words")
            print(f"AVL Time: {testPicker("insert", "AVL", 500, None)} seconds")
            print(f"Dictonary Time: {testPicker("insert", "DIC", 500, None)} seconds\n")

            # 1000 WORDS
            print("Insertion of 1000 words")
            print(f"AVL Time: {testPicker("insert", "AVL", 1000, None)} seconds")
            print(f"Dictonary Time: {testPicker("insert", "DIC", 1000, None)} seconds\n")

            # 5000 WORDS
            print("Insertion of 5000 words")
            print(f"AVL Time: {testPicker("insert", "AVL", 5000, None)} seconds")
            print(f"Dictonary Time: {testPicker("insert", "DIC", 5000, None)} seconds\n")


            # SEARCH TESTS

            print(lineBarrier)
            print("SEARCH".center(50))
            print(lineBarrier)

            # With 50 words find...
            wordToFind = "access"
            print(f'With a 50 words, search for "{wordToFind.title()}"')
            print(f"AVL Time: {testPicker("search", "AVL", 50, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("search", "DIC", 50, wordToFind)} seconds\n")

            # With 100 words find...
            wordToFind = "achievement"
            print(f'With a 100 words, search for "{wordToFind.title()}"')
            print(f"AVL Time: {testPicker("search", "AVL", 100, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("search", "DIC", 100, wordToFind)} seconds\n")

            # With 500 words find...
            wordToFind = "angel"
            print(f'With a 500 words, search for "{wordToFind.title()}"')
            print(f"AVL Time: {testPicker("search", "AVL", 500, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("search", "DIC", 500, wordToFind)} seconds\n")

            # With 1000 words find...
            wordToFind = "baseball"
            print(f'With a 1000 words, search for "{wordToFind.title()}"')
            print(f"AVL Time: {testPicker("search", "AVL", 1000, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("search", "DIC", 1000, wordToFind)} seconds\n")

            # With 5000 words find...
            wordToFind = "five"
            print(f'With a 5000 words, search for "{wordToFind.title()}"')
            print(f"AVL Time: {testPicker("search", "AVL", 5000, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("search", "DIC", 5000, wordToFind)} seconds\n")


            # DELETE TESTS

            print(lineBarrier)
            print("DELETE".center(50))
            print(lineBarrier)

            # With 50 words find...
            wordToFind = "academy"
            print(f'With a 50 words, search for "{wordToFind.title()}" and delete it')
            print(f"AVL Time: {testPicker("delete", "AVL", 50, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("delete", "DIC", 50, wordToFind)} seconds\n")

            # With 100 words find...
            wordToFind = "accounts"
            print(f'With a 100 words, search for "{wordToFind.title()} and delete it"')
            print(f"AVL Time: {testPicker("delete", "AVL", 100, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("delete", "DIC", 100, wordToFind)} seconds\n")

            # With 500 words find...
            wordToFind = "amazon"
            print(f'With a 500 words, search for "{wordToFind.title()} and delete it"')
            print(f"AVL Time: {testPicker("delete", "AVL", 500, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("delete", "DIC", 500, wordToFind)} seconds\n")

            # With 1000 words find...
            wordToFind = "attorney"
            print(f'With a 1000 words, search for "{wordToFind.title()} and delete it"')
            print(f"AVL Time: {testPicker("delete", "AVL", 1000, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("delete", "DIC", 1000, wordToFind)} seconds\n")

            # With 5000 words find...
            wordToFind = "heather"
            print(f'With a 5000 words, search for "{wordToFind.title()}"')
            print(f"AVL Time: {testPicker("delete", "AVL", 5000, wordToFind)} seconds")
            print(f"Dictonary Time: {testPicker("delete", "DIC", 5000, wordToFind)} seconds\n")



            # Get user input
            print()
            userInput = input().title().lstrip()

        
            # Clear terminal in loop
            terminalCleaner()

        # Clear terminal if user returns
        terminalCleaner()

        

    # If file is not found give error and ask user to return to main menu
    except FileNotFoundError:
        while userInput != "B":
            print(lineBarrier)
            print("Cannot find testing file".center(50))
            print(lineBarrier)
            print("Press B to return to menu!")
            print(lineBarrier)

                # Get user input
            userInput = input().title().lstrip()
        
            # Clear terminal in loop
            terminalCleaner()
        # Clear terminal if user returns
        terminalCleaner()
        return
