
#Setup
for x in range(100):
	print(" ")
BookworkCode = "b10" #THIS IS TO PREVENT CRASH IF FUNC 2 IS USED WITHOUT A PAST CODE
MainLoop = "Y"
DIRECTORY = "Documents/Python/SparksMaths/BookworkCheckCodes/"		#Change this to where you want to read and write documents#

#MainLoop
while MainLoop == "Y":

	#Space
	print(" ")
	print(" ")
	
	#input --GET OPERATOR--
	print("---------------------------")
	print("|1| SAVE NEW FILE")
	print("|2| OPEN FILE")
	print("|3| OPEN LAST SAVED")
	print("|4| EXIT")
	print("---------------------------")
	Operator = int(input(">>>"))

	#WRITE
	if Operator == 1:
		#Space
		for x in range(100):
			print(" ")
		
		#Input: BookworkCode and Answer
		BookworkCode = str(input("Enter Bookwork code >>>"))
		Answer = str(input("Enter answer >>>"))
		
		#Open File, Write and Close
		file = open(DIRECTORY + BookworkCode, "w")
		file.writelines(BookworkCode + " ===== "+ Answer + "\n")
		file.close()
		
		#Notice
		print("----------------------")
		print("WROTE TO: " + DIRECTORY + BookworkCode)
		print("----------------------")
		
		#Space
		for x in range(100):
			print(" ")
		
	#OPEN
	elif Operator == 2:
		#Space
		for x in range(100):
			print(" ")
		
		#Input
		BookworkCode = str(input("Enter Bookwork Code >>>"))

		#Open File, Print and Close
		file = open(DIRECTORY + BookworkCode, "r")
		for line in file:
			print(line)
		file.close()
		
		#Stall
		Stall = input(">>>")
		
		#Notice
		print("----------------------")
		print("OPENED: " + DIRECTORY + BookworkCode)
		print("----------------------")
		
		#Space
		for x in range(100):
			print(" ")
		
	#OPEN LAST
	elif Operator == 3:
		#Space
		for x in range(100):
			print(" ")
		
		#Notice, Open, Print and Close
		print("Your last answer was: ")
		file = open(DIRECTORY + BookworkCode, "r")
		for line in file:
			print(line)
		file.close()
		
		#Space
		print(" ")
		
		#Input
		Answer = str(input("Enter new answer >>>"))
		
		#Open File, Write and Close
		file = open(DIRECTORY + BookworkCode, "w")
		file.writelines(BookworkCode + " ===== "+ Answer + "\n")
		file.close()
		
		#Notice
		print("----------------------")
		print("OPENED: " + DIRECTORY + BookworkCode)
		print("WROTE TO: " + DIRECTORY + BookworkCode)
		print("----------------------")
		
		#Space
		for x in range(100):
			print(" ")
		
	#EXIT
	elif Operator == 4:
		#Space
		for x in range(100):
			print(" ")
		MainLoop = "N"
	
	else:
		#input --GET OPERATOR--
		print("THAT IS NOT RECONISED: TRY AGAIN")
		print("|1| SAVE NEW FILE")
		print("|2| OPEN FILE")
		print("|3| OPEN LAST SAVED")
		print("|4| EXIT")
		print(" ")
		Operator = int(input(">>>"))
