from encodings import utf_8
utf_8
import socket
from wAPIgetChar import wMain as wAPIgetChar

def wMain():
	print ("Your HostName: " + socket.gethostname())
	wconnhost = input ("Input HostName: ")
	wconnport0 = input("Input Port: ")
	try:
		wconnport = int(wconnport0)
	except:
		print("ERROR: Input Not a Port")
		return 0
	ws = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return 0