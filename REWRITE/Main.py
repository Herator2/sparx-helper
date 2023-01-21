
# Imports
import os

# Def
SaveDirectory = "Documents/BookworkCodes/"
BookworkCode = "b10"

# Print
print("Save Or Open File?")
print("1 - Save File")
print("2 - Open File")
print("3 - Exit")

# Take Option
Option = str(input(">>>"))

# Save:
if Option.lower() in ["1", "one", "save"]:

    # Get bookwork code to open as
    print("Enter BookworkCode")
    BookworkCode = str(input(">>>"))

    # Make file to save to
    with open(SaveDirectory + BookworkCode, "w+") as File:
        
        # Save answer for later print
        print("Enter Answer")
        File.write(str(print(">>>")))

# Open:
elif Option.lower() in ["2", "two", "open"]:

    # Get bookwork code to open as
    print("Enter BookworkCode")
    BookworkCode = str(input(">>>"))

    # Make file to save to
    with open(SaveDirectory + BookworkCode, "r") as File:
        
        # Read file
        File.read()

        # Print as BookworkCode: Ans    e.g. b10: 6
        print(BookworkCode + ":", File)

# Exit
elif Option.lower() in ["3", "three", "quit", "close", "exit"]:
    
    # Exit function
    exit()
