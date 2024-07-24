import os

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
    return path


# Print Menu
def printMenu():
    spacer = "=" * os.get_terminal_size()[0]
    print(f"{spacer}\nBookwork Code | {bookwork_code.upper()}\n{spacer}")
    option = str(
        input(
            "n | Next - Move on to next section\no | Open - Search For Bookwork Code\nc | Code - Overwrite Bookwork Code\ne | Exit - Exit Program\n  | Any - Enter Answer For Bookwork Code\n  | >>> "
        )
    )
    return option


# Save Bookwork Code
def saveAnswer(answer, bookwork_code):
    with open(os.path.join(save_directory, bookwork_code.lower()), "w+") as f:
        f.write(answer)


# Load Bookwork Code
def loadAnswer(bookwork_code):
    if get_filename(bookwork_code) in os.listdir(save_directory):
        with open(os.path.join(save_directory, bookwork_code.lower()), "r") as f:
            ans = f.read()
            return ans

# Turn bookwork code into its text filename
def get_filename(bookwork_code):
    filename = bookwork_code.lower()
    filename += ".txt"
    return filename

# Guess next code
def getNextCode(lastcode):
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
    ]
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


# Setup Variables
bookwork_code = "1A"
save_directory_name = "data"
save_directory = parsePath(f"~/{save_directory_name}")

# Make data folder if it does not exist
if save_directory_name not in os.listdir(parsePath("~/")):
    os.mkdir(save_directory)

# Main Loop
while True:
    # Get user input from menu
    clear()
    raw_option = printMenu()
    options = raw_option.lower().split()

    # Do not do anything
    if len(options) == 0:
        continue

    # Exit command
    if options[0] in ["exit", "e"] and len(options) == 1:
        exit()
    
    # Next section
    if options[0] in ["next", "n"] and len(options) == 1:
        bookwork_code = next_section(bookwork_code)
        continue

    # Change Bookwork Code
    if options[0] in ["code", "c"]:
        if len(options) > 1:
            bookwork_code = options[1]
            continue
        bookwork_code = str(input("Please enter Bookwork Code\n>>> "))
        continue

    # Open
    if options[0] in ["open", "o"]:
        open_code = ""
        if len(options) > 1 and len(options[1]) == 2:
            open_code = options[1]
        else:
            open_code = str(input("Enter Bookwork Code\n>>> "))
        ans = loadAnswer(open_code)
        if ans == None:
            print("Bookwork Code Not Found")
        else:
            print(open_code.lower() + ":", ans)
        input(">>> ")
        continue

    # Save Answer
    saveAnswer(raw_option, bookwork_code)

    # Get next code
    bookwork_code = getNextCode(bookwork_code)
