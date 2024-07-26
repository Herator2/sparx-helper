import os

# Clear screen
def clear() -> None:
    for x in range(os.get_terminal_size()[1]):
        print("")


# Get directory
def getDirectory() -> str:
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("/src", "")
    return path


# Change path to absolute from relative
def parsePath(path: str) -> str:
    if "~" in path:
        path = path.replace("~/", "")
        path = os.path.join(getDirectory(), path)
        return path
    return path


# Print input menu
def printMenu() -> str:
    print("┌─────┬" + ("─" * (os.get_terminal_size()[0] - 7 - 8)) + "┬──────┐")
    print("│ KEY │ DESCRIPTION" + (" " * (os.get_terminal_size()[0] - 30)) + f"{bookwork_code} │ CODE │")
    print("├─────┼" + ("─" * (os.get_terminal_size()[0] - 7 - 8)) + "┴──────┘")
    option = str(
        input(
            "│  n  │ Move on to next Section\n│  o  │ Search for Bookwork Code\n│  c  │ Overwrite Bookwork Code\n│  e  │ Exit\n│  ~  │ Enter Answer\n│     │ >>> "
        )
    )
    return option


# Save Bookwork Code
def saveAnswer(answer: str, bookwork_code: str) -> None:
    bookwork_code = verifyBookworkPrompt(bookwork_code)
    with open(os.path.join(save_directory, getFilename(bookwork_code)), "w") as f:
        f.write(answer)


# Load Bookwork Code
def loadAnswer(bookwork_code: str) -> str|None:
    if getFilename(bookwork_code) in os.listdir(save_directory):
        with open(os.path.join(save_directory, getFilename(bookwork_code)), "r") as f:
            ans = f.read()
            return ans

# Turn bookwork code into its text filename
def getFilename(bookwork_code: str) -> str:
    filename = bookwork_code.lower()
    filename += ".txt"
    return filename

# Guess next code
def getNextCode(lastcode: str) -> str:
    lastcode = verifyBookworkPrompt(lastcode)
    abc = "abcdefghijklmnopqrstuvwxyz"
    index = abc.index(lastcode[1].lower())
    index += 1
    if index >= len(abc):
        index = 0
    bookwork_code = lastcode[0] + abc[index].upper()
    bookwork_code = verifyBookworkPrompt(bookwork_code)
    return bookwork_code


# Switch to next section
def next_section(bookwork_code: str) -> str:
    num = bookwork_code[0]
    num = int(num)
    num = num + 1
    bookwork_code = str(num) + "A"
    bookwork_code = verifyBookworkPrompt(bookwork_code)
    return bookwork_code

# Check if a bookwork code is in a valid format
def verifyBookworkCode(bookwork_code: str) -> bool:
    if len(bookwork_code) != 2:
        return False
    if bookwork_code[0] not in "123456789":
        return False
    if bookwork_code[1].lower() not in "abcdefghijk":
        return False
    return True

# Check if bookwork code is valid and promot if it is not
def verifyBookworkPrompt(bookwork_code: str) -> str:
    while not verifyBookworkCode(bookwork_code):
        bookwork_code = styledInput("Re-enter a valid bookwork code", "?")
    bookwork_code = bookwork_code.upper() # Make sure second character is upper case
    return bookwork_code


# Take input using a prompt with fancy styling to match the main menu
def styledInput(prompt, symbol="?"):
    # Sorry for anyone attempting to read this
    print("├" + ("─" * (len(symbol) + 4)) + "┼" + ("─" * (len(prompt) + 2)) + "┐")
    print("│  " + symbol + "  │ " + prompt + " │")
    print("├" + ("─" * (len(symbol) + 4)) + "┼" + ("─" * (len(prompt) + 2)) + "┘")
    return input("│" + (" " * (len(symbol) + 4)) + "│" + " >>> ")

def styledPrint(prompt, symbol="!"):
    print("│  " + symbol + "  │ " + prompt + (" " * (os.get_terminal_size()[0] - len(symbol) - len(prompt) - 8)) + "│")

def displayAlert(text):
    alert_length = len(text) + 4
    whitespace = ((os.get_terminal_size()[0] // 2) - (alert_length // 2)) * " "
    print(whitespace + "╔═" + ("═" * len(text)) + "═╗")
    print(whitespace + "║ " + text + " ║")
    print(whitespace + "╚═" + ("═" * len(text)) + "═╝")

# Setup Variables
bookwork_code = "1A"
save_directory_name = "data"
save_directory = parsePath(f"~/{save_directory_name}")
alerts = []

# Make data folder if it does not exist
if save_directory_name not in os.listdir(parsePath("~/")):
    os.mkdir(save_directory)

# Main Loop
while True:
    # Clear screen and print alerts
    clear()
    for alert in alerts:
        displayAlert(alert)
    alerts = []

    # Get user input from menu
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
        alerts.append(f"Moved to next section")
        continue

    # Change Bookwork Code
    if options[0] in ["code", "c"]:
        if len(options) > 1:
            bookwork_code = options[1]
        else:
            bookwork_code = styledInput("Enter Bookwork Code to change to", "?")
        bookwork_code = verifyBookworkPrompt(bookwork_code)
        alerts.append(f"Changed Bookwork Code to {bookwork_code}")
        continue

    # Open
    if options[0] in ["open", "o"]:
        open_code = ""
        if len(options) > 1 and len(options[1]) == 2:
            open_code = options[1]
        else:
            open_code = styledInput("Enter Bookwork Code to read answer from", "?")
        ans = loadAnswer(open_code)
        if open_code == "":
            alerts.append("Skipped opening blank code...")
            continue
        elif ans == None:
            alerts.append(f"No data found for code: {open_code}")
            continue
        styledPrint(open_code.upper() + ": " + ans, "!")
        styledInput("Press enter to continue...")
        continue

    # Save Answer
    saveAnswer(raw_option, bookwork_code)
    alerts.append(f"Saved answer: {raw_option} to {bookwork_code.upper()}")

    # Get next code
    bookwork_code = getNextCode(bookwork_code)
