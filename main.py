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
reset_code = "1A"
bookwork_code = reset_code
debug_log = False

# Clear Screen NEEDS WORK
def clear():
    for x in range(os.get_terminal_size()[1]):
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
            "n | Next - Move on to next section\no | Open - Search For Bookwork Code\nc | Code - Overwrite Bookwork Code\ne | Exit - Exit Program\n  | Any - Enter Answer For Bookwork Code\n  | >>> "
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
    index = abc.index(lastcode[1].lower())
    index += 1
    bookwork_code = lastcode[0] + abc[index].upper()
    return bookwork_code


# Switch to next section
def next_section(bookwork_code):
    num = bookwork_code[0]
    num = int(num)
    num = num + 1
    bookwork_code = str(num) + "A"
    return bookwork_code

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
print("Got To Main Loop")
if debug_log:
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
    if option.lower() in ["exit", "e"]:
        exit()
    # Next section
    elif option.lower() in ["next", "n"]:
        bookwork_code = next_section(bookwork_code)
        skip = True
    # Change Bookwork Code
    elif option.lower() in ["code", "c"]:
        bookwork_code = str(input("Enter Bookwork Code\n>>> "))
        skip = True
    # Open
    elif option.lower() in ["open", "o"]:
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
