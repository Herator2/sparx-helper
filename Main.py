
# Imports
import os

# Def
SaveDirectory = "Documents/BookworkCodes/"
BookworkCode = "b10"

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

    # Ask to automatically make folders incase of different error
    print("Automatically Create Nessesary Folders? y|n")
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

    # Print
    os.system("clear")
    print("Save Or Open File?")
    print("1 - Save File")
    print("2 - Open File")
    print("3 - Exit")

    # Take Option
    Option = str(input(">>>"))
    os.system("clear")

    # Save:
    if Option.lower() in ["1", "one", "save"]:

        # Get bookwork code to open as
        print("Enter BookworkCode")
        BookworkCode = str(input(">>>"))

        # Make file to save to
        with open(SaveDirectory + BookworkCode.lower(), "w+") as File:
            
            # Save answer for later print
            os.system("clear")
            print("Enter Answer")
            File.write(str(input(">>>")))

    # Open:
    elif Option.lower() in ["2", "two", "open"]:

        # Get bookwork code to open as
        print("Enter BookworkCode")
        BookworkCode = str(input(">>>"))

        # If file exists
        try:
            # Make file to save to
            with open(SaveDirectory + BookworkCode.lower(), "r") as File:
                
                # Read file
                Ans = File.read()

                # Print as BookworkCode: Ans    e.g. b10: 6
                print(BookworkCode.lower() + ":", Ans)

            # Stall
            input(">>>")

        # No file exists
        except Exception as ErrorMsg:

            # Msg
            print(ErrorMsg)
            print("Maybe You Forgot To Save That One Or Typed it In Wrong?")

            # Stall
            input(">>>")

    # Exit
    elif Option.lower() in ["3", "three", "quit", "close", "exit"]:
        
        # Exit function
        exit()
