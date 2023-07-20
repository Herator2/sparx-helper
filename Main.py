import os
import json


# Move To Home Directory
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
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]  # THIS ABC DOES NOT CONTAIN A I OR AN O
BookworkCode = "Start"  # Preset Bookwork Code At Startup
Skip = False  # Used To Skip Bookwork Code Updating


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


# Config Read
try:
    with open(os.path.join(getDirectory(), "config.json"), "r") as config:
        # Load Config
        config = json.load(config)
        SaveDirectory = config["savedir"]
        SaveDirectory = parsePath(SaveDirectory)

# Config Auto Creation
except:
    with open(os.path.join(getDirectory(), "config.json"), "w") as config:
        defualtConfig = {
            "SaveDirectory": "~/BookworkCodes"
        }
        json.dump(defualtConfig, config, indent=4)
        SaveDirectory = parsePath(defualtConfig["SaveDirectory"])

# Test Folder
try:
    with open(os.path.join(SaveDirectory, "Temp"), "w+") as File:
        File.read()

# Create Folder
except Exception as ErrorMsg:
    print(ErrorMsg)
    os.mkdir(SaveDirectory)
    print("Made Folder " + SaveDirectory)


# Loop
while True:
    clear()

    # NEW: Auto BookworkCode Guess
    if not Skip:
        try:
            if (
                BookworkCode != "Start"
                and BookworkCode[0] != "z"
                and len(BookworkCode) == 3
            ):
                NewBookworkCode = []
                for char in BookworkCode.lower():
                    NewBookworkCode.append(char)

                # If Nine
                if NewBookworkCode[1] == "9":
                    NewBookworkCode[1] = "0"  # Set Num To 0
                    NewBookworkCode[2] = str(
                        int(NewBookworkCode[2]) + 1
                    )  # Increment OTHER Num
                else:
                    # Increment Num
                    NewBookworkCode[1] = str(int(NewBookworkCode[1]) + 1)

                # Work Out Letter
                NewBookworkCode[0] = abc[
                    int(NewBookworkCode[1]) + int(NewBookworkCode[2])
                ]
                BookworkCode = "".join(NewBookworkCode)  # Parse
            else:
                BookworkCode = "b01"

            if len(BookworkCode) != 3:
                BookworkCode = "b01"

        # NORMAL INPUT If Guess Fails To Run
        except Exception as ErrorMSG:
            BookworkCode = str(input(f"{ErrorMSG}\nENTER BOOKWORK CODE MANUALLY\n>>> "))
            clear()
    else:
        Skip = False

    # MENU
    print(
        f"==============================\nCODE | {BookworkCode.upper()}\n=============================="
    )
    Option = str(
        input(
            "TYPE | CODE - Overwrite BkwrkCode\nTYPE | OPEN - Search For BkwrkCode\nTYPE | ANY - Enter Answer\n     | >>> "
        )
    )

    # Bookwork Code
    if Option.lower() in ["code"]:
        BookworkCode = str(input("ENTER BOOKWORK CODE MANUALLY\n>>> "))
        Option = str(input("ENTER ANSWER\n>>> "))

    # Open:
    if Option.lower() in ["open"]:
        TempBookworkCode = str(input("ENTER BOOKWORK CODE MANUALLY\n>>> "))

        # If file exists
        try:
            # Make file to save to
            with open(SaveDirectory + TempBookworkCode.lower(), "r") as File:
                # Read file
                Ans = File.read()

                # Print as BookworkCode: Ans    e.g. b10: 6
                print(TempBookworkCode.lower() + ":", Ans)

            # Stall
            input(">>> ")

            # Skip Bookwork Code Updation
            # This means that the auto bookwork code pattern stays relevant / accurate
            Skip = True

        # No file exists
        except Exception as ErrorMsg:
            # Msg
            print(ErrorMsg)
            print("404: CODE NOT FOUND")
            input(">>> ")

    # Save Ans
    else:
        with open(SaveDirectory + BookworkCode.lower(), "w+") as File:
            File.write(Option)
