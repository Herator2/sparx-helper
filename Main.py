
# CHANGE THESE:
Linux = True
SaveDirectory = "Documents/School/Math/AutoBookworkCodes/"

# Imports
import os

# Reset Directory
os.chdir("/home/[USER]/")

# Def
BookworkCode = "Start"  # Preset Bookwork Code At Startup
Skip = False  # Used To Skip Bookwork Code Updating
# THIS ABC DOES NOT CONTAIN A I OR AN O
# THESE DO NOT SEEM TO SHOW UP IN BOOKWORK CODES
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This is used multiple times
def BookworkCodeInput():
    global BookworkCode
    BookworkCode = str(input("Enter BookworkCode\n>>>"))

# Automatic folder creation
try:

    # See if folder exists
    with open(SaveDirectory + "Temp", "w+") as File:

        # Read file
        File.read()

        # Write a line
        File.write("If you see this, Automatic folder creation did not happen")

# If folder doesn't exist
except Exception as ErrorMsg:

    # Print msg
    print(ErrorMsg)

    # Ask to automatically make folders in case of different error
    print("Automatically Create Necessary Folders? y|n")
    Option = str(input(">>>"))

    # Start Folder Creation
    if Option.lower() in ["y", "yes", "yea", "ye", "yeah", "1"]:

        # Msg
        print("Automatic Folder Creation Starting")

        # Make Folders
        os.mkdir(SaveDirectory)

        # Finish msg
        print("Made Folder " + SaveDirectory)
        print("Finished Automatic Folder Creation")

    # Skip
    else:
        
        # This is just for a slightly different msg
        if Option.lower() in ["n", "no", "nope", "0", "2"]:
            print("Skipping...")
        else:
            print("Unrecognised Answer: Skipping...")
            
# Loop
while True:

    for x in range(30):
        print()

    # NEW: Auto BookworkCode Guess
    if not Skip:
        try:
            if BookworkCode != "Start" and BookworkCode[0] != 'z' and len(BookworkCode) == 3: 
                NewBookworkCode = []
                for char in BookworkCode.lower():
                    NewBookworkCode.append(char)

                # If Nine
                if NewBookworkCode[1] == '9':
                    NewBookworkCode[1] = '0'  # Set Num To 0
                    NewBookworkCode[2] = str(int(NewBookworkCode[2])+1)  # Increment OTHER Num
                else:
                    # Increment Num
                    NewBookworkCode[1] = str(int(NewBookworkCode[1])+1)  

                # Work Out Letter
                NewBookworkCode[0] = abc[int(NewBookworkCode[1])+int(NewBookworkCode[2])]
                BookworkCode = "".join(NewBookworkCode)  # Parse
                print(f"CODE | {BookworkCode}\n==============================")
            else:
                raise Exception("CONDITIONS NOT MET FOR AUTO GUESS")
            
            if len(BookworkCode) != 3:
                raise Exception("BOOKWORK CODE HAS OVERFLOWED")

        # NORMAL INPUT If Guess Fails To Run
        except Exception as ErrorMSG:
            BookworkCode = str(input(f"{ErrorMSG}\nENTER BOOKWORK CODE MANUALLY\n>>>"))
    else:  Skip = False

    # MENU
    Option = str(input("TYPE | CODE - Overwrite BkwrkCode\nTYPE | OPEN - Search For BkwrkCode\nTYPE | ANY - Enter Answer\n     | >>>"))

    # Bookwork Code
    if Option.lower() in ["code"]:
        BookworkCode = str(input("ENTER BOOKWORK CODE MANUALLY\n>>>"))
        Option = str(input("ENTER ANSWER\n>>>"))

    # Open:
    if Option.lower() in ["open"]:
        TempBookworkCode = str(input("ENTER BOOKWORK CODE MANUALLY\n>>>"))

        # If file exists
        try:
            # Make file to save to
            with open(SaveDirectory + TempBookworkCode.lower(), "r") as File:
                
                # Read file
                Ans = File.read()

                # Print as BookworkCode: Ans    e.g. b10: 6
                print(TempBookworkCode.lower() + ":", Ans)

            # Stall
            input(">>>")

            # Skip Bookwork Code Updation
            # This means that the auto bookwork code pattern stays relevant / accurate
            Skip = True

        # No file exists
        except Exception as ErrorMsg:

            # Msg
            print(ErrorMsg)
            print("404: CODE NOT FOUND")
            input(">>>")

    # Save Ans
    else:
        with open(SaveDirectory + BookworkCode.lower(), "w+") as File:
            File.write(Option)
