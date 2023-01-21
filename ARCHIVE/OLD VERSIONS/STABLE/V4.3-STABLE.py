
# Setup
from datetime import date
from datetime import datetime
today = date.today()
Date = today.strftime("%d/%m/%Y")
now = datetime.now()
Time = now.strftime("%d/%m/%Y - %H:%M:%S")
BookworkCode = "b10"  # THIS IS TO PREVENT CRASH IF FUNC 3 IS USED WITHOUT A PAST CODE
MainLoop = "Y"
# Space
for x in range(100):
	print(" ")
# CHANGE THESE TO YOUR DIRECTORY

# Change this to where you want to read and write documents
DIRECTORY = "Documents/SparksMaths/BookworkCodes"
# Change this to where you want to save logs
LOGDIRECTORY = "Documents/SparksMaths/Log.txt"

# Startup Logs		#Open Log File, Write and Close
file = open(LOGDIRECTORY, "a")
file.writelines("\n" "-----------------------------")
file.writelines("\n" "STARTUP AT " + Time)
file.close()


# MainLoop
while MainLoop == "Y":

	# input --GET OPERATOR--
	print("|===|=============================")
	print("| 1 | - Save New File")
	print("| 2 | - Open a file")
	print("| 3 | - Open last saved file")
	print("| 4 | - View Logs")
	print("| 5 | - Exit")
	print("|===|=============================")
	Operator = str(input("| ? | >>>"))

	# WRITE
	if Operator == "1":

		# Space
		for x in range(100):
			print(" ")

		# Input: BookworkCode
		print("|===|=============================")
		BookworkCode = str(input("| ? | - Enter Bookwork code >>>"))

		# Input: Answer
		print("|===|=============================")
		Answer = str(input("| ? | - Enter answer >>>"))

		# Open File, Write and Close
		file = open(DIRECTORY + BookworkCode, "w")
		file.writelines(BookworkCode + " ===== " + Answer)
		file.close()
		
		# Update Time
		today = date.today()
		Date = today.strftime("%d/%m/%Y")
		now = datetime.now()
		Time = now.strftime("%d/%m/%Y - %H:%M:%S")

		# Open Log File, Write and Close
		file = open(LOGDIRECTORY, "a")
		file.writelines("\n" "WROTE TO: " + DIRECTORY + BookworkCode + "AT " + Time)
		file.close()

		# Space
		for x in range(100):
			print(" ")
		
	# OPEN
	elif Operator == "2":
		# Space
		for x in range(100):
			print(" ")
		
		# Input
		print("|===|=============================")
		BookworkCode = str(input("| ? | - Enter Bookwork Code >>>"))
		print("|===|=============================")

		# Open File, Print and Close
		print(" ")
		file = open(DIRECTORY + BookworkCode, "r")
		for line in file:
			print("| ! | - ", line)
		file.close()
		
		# Stall
		print("|===|=============================")
		Stall = input("| - | >>>")

		# Update Time
		today = date.today()
		Date = today.strftime("%d/%m/%Y")
		now = datetime.now()
		Time = now.strftime("%d/%m/%Y - %H:%M:%S")
		
		# Open Log File, Write and Close
		file = open(LOGDIRECTORY, "a")
		file.writelines("\n" "OPENED: " + DIRECTORY + BookworkCode + " AT " + Time)
		file.close()

		# Space
		for x in range(100):
			print(" ")
		
	# OPEN LAST
	elif Operator == "3":

		# Space
		for x in range(100):
			print(" ")

		# Notice, Open, Print and Close
		print("|===|=============================")
		print("| - | - Your last answer was: ")
		print(" ")

		file = open(DIRECTORY + BookworkCode, "r")
		for line in file:
			print("| ! | - ", line)
		file.close()

		# Update Time
		today = date.today()
		Date = today.strftime("%d/%m/%Y")
		now = datetime.now()
		Time = now.strftime("%d/%m/%Y - %H:%M:%S")
		
		# Open Log File, Write and Close
		file = open(LOGDIRECTORY, "a")
		file.writelines("\n" "OPENED: " + DIRECTORY + BookworkCode + " AT " + Time)
		file.close()
		
		# Input
		print("|===|=============================")
		Answer = str(input("| ? | - Enter new answer >>>"))

		# Update Time
		now = datetime.now()
		Time = now.strftime("%d/%m/%Y - %H:%M:%S")
		
		# Open File, Write and Close
		file = open(DIRECTORY + BookworkCode, "w")
		file.writelines(BookworkCode + " ===== " + Answer + "\n")
		file.close()
		
		# Open Log File, Write and Close
		file = open(LOGDIRECTORY, "a")
		file.writelines("\n" "WROTE TO: " + DIRECTORY + BookworkCode + " AT " + Time)
		file.close()

		# Space
		for x in range(100):
			print(" ")

	# LOGS
	elif Operator == "4":

		# Space
		for x in range(100):
			print(" ")

		print("|===|=============================")
		# Open File, Print and Close
		file = open(LOGDIRECTORY, "r")
		for line in file:
			print("| ! | - ", line)
		file.close()

		# Update Time
		today = date.today()
		Date = today.strftime("%d/%m/%Y")
		now = datetime.now()
		Time = now.strftime("%d/%m/%Y - %H:%M:%S")

		# Open Log File, Write and Close
		file = open(LOGDIRECTORY, "a")
		file.writelines("\n" "OPENED LOGS AT: " + LOGDIRECTORY + "Log.txt" + " AT " + Time)
		file.close()

		# Stall
		print("|===|=============================")
		Stall = input("| ? | >>>")

		# Space
		for x in range(100):
			print(" ")

	# EXIT
	else:
		
		print("|===|=============================")
		MainLoop = "N"

		# Update Time
		today = date.today()
		Date = today.strftime("%d/%m/%Y")
		now = datetime.now()
		Time = now.strftime("%d/%m/%Y - %H:%M:%S")

		# Open Log File, Write and Close
		file = open(LOGDIRECTORY, "a")
		file.writelines("\n" "NORMAL CLOSE AT " + Time)
		file.close()
