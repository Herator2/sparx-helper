import os
import json


# Setup
abc = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "a",
]
reset_code = "b10"
bookwork_code = reset_code


# Clear Screen NEEDS WORK
def clear():
    for x in range(30):
        print("")


# Get directory
def getDirectory():
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("/src", "")
    return path


# Change path to absolute from relative
def parsePath(path):
    if "~" in path:
        path = path.replace("~/", "")
        path = os.path.join(getDirectory(), path)
        return path
    else:
        return path


# Print Menu
def printMenu():
    spacer = "=" * os.get_terminal_size()[0]
    print(f"{spacer}Bookwork Code | {bookwork_code.upper()}\n{spacer}")
    option = str(
        input(
            " | Code - Overwrite Bookwork Code\n | Open - Search For Bookwork Code\n | Exit - Exit Program\n | Any - Enter Answer For Bookwork Code\n | >>> "
        )
    )
    return option


# Save Bookwork Code
def saveAnswer(answer, bookwork_code):
    with open(os.path.join(SaveDirectory, bookwork_code.lower()), "w+") as File:
        File.write(answer)


# Load Bookwork Code
def loadAnswer(bookwork_code):
    try:
        with open(os.path.join(SaveDirectory, bookwork_code.lower()), "r") as File:
            ans = File.read()
            return ans
    except FileNotFoundError:
        return None


# Guess next code
def getNextCode(lastcode):
    # Reset Bookwork Code
    if lastcode[0] == "a" or len(lastcode) > 3:
        print(lastcode)
        result = reset_code
    else:
        construct_code = []
        for char in lastcode.lower():
            construct_code.append(char)
        if construct_code[1] == "9":
            construct_code[1] = "0"  # Set Num To 0
            construct_code[2] = str(int(construct_code[2]) + 1)
        else:
            construct_code[1] = str(int(construct_code[1]) + 1)
        construct_code[0] = abc[int(construct_code[1]) + int(construct_code[2])]
        result = "".join(construct_code)  # Parse
        print(result)
        print(construct_code)
    return result


# Config Read
try:
    with open(os.path.join(getDirectory(), "config.json"), "r") as config:
        # Load Config
        config = json.load(config)
        SaveDirectory = config["SaveDirectory"]
        SaveDirectory = parsePath(SaveDirectory)
        print("Loaded config from config.json")

# Config Auto Creation
except:
    with open(os.path.join(getDirectory(), "config.json"), "w") as config:
        defualtConfig = {"SaveDirectory": "~/BookworkCodes"}
        json.dump(defualtConfig, config, indent=4)
        SaveDirectory = parsePath(defualtConfig["SaveDirectory"])
        print("Made file config.json")


# Test BookworkCodes
try:
    with open(os.path.join(SaveDirectory, "Temp"), "w+") as File:
        File.read()

# Create Folder
except Exception as error_msg:
    os.mkdir(SaveDirectory)
    print("Made Folder " + SaveDirectory)


# Startup Print
print("Succsessfully Started Application")
print("Press ENTER to start")
input(">>>")


# Main Loop
while True:
    # Setup Skip
    skip = False

    # Menu
    clear()
    option = printMenu()
    # Exit
    if option.lower() in ["exit"]:
        exit()
    # Change Bookwork Code
    elif option.lower() in ["code"]:
        bookwork_code = str(input("Enter Bookwork Code\n>>> "))
        skip = True
    # Open
    elif option.lower() in ["open"]:
        temp_code = str(input("Enter Bookwork Code\n>>> "))
        ans = loadAnswer(temp_code)
        if ans == None:
            print("Bookwork Code Not Found")
        else:
            print(temp_code.lower() + ":", ans)
        input(">>> ")
        skip = True
    # Save Ans
    else:
        saveAnswer(option, bookwork_code)

    # Get Next Code
    if not skip:
        bookwork_code = getNextCode(bookwork_code)
