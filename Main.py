from encodings import utf_8
utf_8
import os
from modules import wgetChar

os.system("title cmdChat v0.1 by wyf9 2023.3.18")

print ("cmdChat Main Menu")
print ("a / 1. Start a Server")
print ("b / 2. Join a Server")
print ("c / 3. Single Chat")
print ("q / 0. Quit")
print ("\n")

while True: 
	wChar = wgetChar.wMain()

	match wChar:

		case "a" | "1":
			print ("Server Mode Not Available.")
			print ("\n")

		case "b" | "2":
			print ("Console Mode Not Available.")
			print ("\n")

		case "c" | "3":
			print ("Single Chat Mode")
			print ("\n")

		case "q" | "0":
			print ("Quitting Program...")
			print ("\n")
			break

os.system("title    ")
exit