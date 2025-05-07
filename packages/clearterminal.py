import os, platform

def terminalCleaner():
    # Added OS to clear terminal on start up (Just a cleaner look)

    # If OS Windows clear terminal by "CLS" 
    # Otherwise, use "Clear"

    clearCommand = "cls" if platform.system() == "Windows" else "clear"
    os.system(clearCommand)
