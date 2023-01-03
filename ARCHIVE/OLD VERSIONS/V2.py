#Setup
MainLoop = "Y"
DIRECTORY = "Documents/Python/SparksMaths/BookworkCheckCodes/"		#Change this to where you want to read and write documents
print("Welcome!")

#MainLoop
while MainLoop == "Y" or MainLoop == "Yes" or MainLoop == "yes" or MainLoop == "YES" or MainLoop == "y":
	
	#Space
	print(" ")
	
	#Input
	BookworkCode = str(input("Enter Bookwork Code Or Type 'Open' To Search >>>"))
	
	#Open
	if BookworkCode == "Open" or BookworkCode == "open" or BookworkCode == "OPEN" or BookworkCode == "O" or BookworkCode == "o":
		
		#Space
		for x in range(25):
			print(" ")
			
		#Input
		BookworkCode = str(input("Enter The Bookwork Code You Want To Search >>>"))
		
		#Space
		for x in range(25):
			print(" ")
		
		#Open File
		file = open(DIRECTORY + BookworkCode, "r")
		
		#Print
		for line in file:
			print(line)
		
		#Close File
		file.close()
		
		#Notice
		print("OPENED: " + DIRECTORY + BookworkCode)
		print("")
	
	#Write
	else:	
	
		#Input
		Answer = str(input("Enter answer >>>"))
		
		#Open File
		file = open(DIRECTORY + BookworkCode, "w")

		#Write
		file.writelines(BookworkCode + " ===== "+ Answer + "\n")

		#Close File
		file.close()
		
		#Space
		for x in range(25):
			print(" ")
		
		#Notice
		print("WROTE TO: " + DIRECTORY + BookworkCode)
		print("")
	
	#Repeat MainLoop
	MainLoop = input("Repeat? >>>")
	while MainLoop != "Y" and MainLoop != "Yes" and MainLoop != "yes" and MainLoop != "YES" and MainLoop != "y" and MainLoop != "N" and MainLoop != "No" and MainLoop != "no" and MainLoop != "NO" and MainLoop != "n":
		MainLoop = input("Input Y or N >>>")
		
	#Space
	for x in range(30):
		print(" ")
