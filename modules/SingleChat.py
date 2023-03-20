from encodings import utf_8
utf_8
import os
from Sources import wAPIgetChar
from Sources import SCComputerA
from Sources import SCComputerB

def wMain():
	os.system ("title pyChat v0.1 by wyf9 2023.3.19 - Single Chat")
	print ("Please select:")
	print ("a / 1. Computer A")
	print ("b / 2. Computer B")
	print ("q / 0. Back to Root Menu")
	print (" ")

	while True:
		wSingleChatMainChar = wAPIgetChar.wMain()

		match wSingleChatMainChar:

			case "a" | "1":
				print("--------------------------------")
				print ("Computer A")
				SCComputerA.wMain()
				print("--------------------------------")

			case "b" | "2":
				print("--------------------------------")
				print ("Computer B")
				SCComputerB.wMain()
				print("--------------------------------")

			case "q" | "0":
				print ("Back to pyChat Root Menu")
				break
	return 0