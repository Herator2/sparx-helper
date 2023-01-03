
# Setup
from datetime import date
from datetime import datetime
for x in range(100):
	print(" ")
today = date.today()
Date = today.strftime("%d/%m/%Y")
now = datetime.now()
Time = now.strftime("%d/%m/%Y - %H:%M:%S")
BookworkCode = "b10"  # THIS IS TO PREVENT CRASH IF FUNC 3 IS USED WITHOUT A PAST CODE
MainLoop = "Y"

# CHANGE THESE TO YOUR DIRECTORY

# Change this to where you want to read and write documents
DIRECTORY = "Documents/Python/SparksMaths/BookworkCheckCodes/"
# Change this to where you want to save logs
LOGDIRECTORY = "Documents/Python/SparksMaths/LOGS/Log.txt"

# Startup Logs		#Open Log File, Write and Close
file = open(LOGDIRECTORY, "a")
file.writelines("\n" "-----------------------------")
file.writelines("\n" "STARTUP AT " + Time)
file.close()


# MainLoop
while MainLoop == "Y":

	# input --GET OPERATOR--
	print("---------------------------")
	print("|1| SAVE NEW FILE")
	print("|2| OPEN FILE")
	print("|3| OPEN LAST SAVED")
	print("|4| VIEW LOGS")
	print("|5| EXIT")
	print("---------------------------")
	Operator = int(input(">>>"))

	# WRITE
	if Operator == 1:
		# Space
		for x in range(100):
			print(" ")
		
		# Input: BookworkCode
		BookworkCode = str(input("Enter Bookwork code >>>"))

		# Input: Answer
		Answer = str(input("Enter answer >>>"))

		# Open File, Write and Close
		file = open(DIRECTORY + BookworkCode, "w")
		file.writelines(BookworkCode + " ===== " + Answer + "\n")
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
	elif Operator == 2:
		# Space
		for x in range(100):
			print(" ")
		
		# Input
		BookworkCode = str(input("Enter Bookwork Code >>>"))

		# Open File, Print and Close
		file = open(DIRECTORY + BookworkCode, "r")
		for line in file:
			print(line)
		file.close()
		
		# Stall
		Stall = input(">>>")

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
	elif Operator == 3:
		# Space
		for x in range(100):
			print(" ")
		
		# Notice, Open, Print and Close
		print("Your last answer was: ")
		file = open(DIRECTORY + BookworkCode, "r")
		for line in file:
			print(line)
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

		# Space
		print(" ")
		
		# Input
		Answer = str(input("Enter new answer >>>"))

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
	elif Operator == 4:
		# Space
		for x in range(100):
			print(" ")

		# Open File, Print and Close
		file = open(LOGDIRECTORY, "r")
		for line in file:
			print(line)
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
		Stall = input(">>>")

		# Space
		for x in range(100):
			print(" ")

	# EXIT
	elif Operator == 5:
		# Space
		for x in range(100):
			print(" ")
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
	
	else:
		# input --GET OPERATOR--

		# Space
		for x in range(100):
			print(" ")
		MainLoop = "N"

		print("THAT IS NOT RECOGNISED: TRY AGAIN")
