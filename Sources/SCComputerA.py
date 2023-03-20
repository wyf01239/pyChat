from encodings import utf_8
utf_8
import socket
import os
import datetime
import _thread
from Sources import wAPIgetChar

ws = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def wMain():
    os.system ("title pyChat v0.1 by wyf9 2023.3.19 - Single Chat - Computer A")
    print ("Your HostName: " + socket.gethostname())
    whostip = socket.gethostbyname(socket.gethostname())
    print ("Your Host IP: " + whostip)
    wport0 = input ("Input Your Port: 91__\n>>")
    wBhost = input ("Input Partner Host: ")
    wBport0 = input("Input Partner Port: 92__\n>>")
    try:
        wBport1 = str(92) + wBport0
        wBport = int(wBport1)
    except ValueError:
        print("ERROR: Input Not a Port")
        return 0
    try:
        wport1 = str(91) + str(wport0)
        wport = int(wport1)
    except ValueError:
        print("ERROR: Input Not a Port")
        return 0
    print ("Press any key to Start Listen, q / 0 to Back...")
    wyn = wAPIgetChar.wMain()
    if wyn == "q":
        print("Listen Canceled.")
        return 0
    elif wyn == "0":
        print("Listen Canceled.")
        return 0
    else:
        print ("Starting Listen...")
    wthArgs = ("launch", wBhost, wBport)
    _thread.start_new_thread(wDef, wthArgs)
    os.system ("title pyChat v0.1 by wyf9 2023.3.19 - Single Chat - Computer A - Get")
    wsbind = whostip, wport
    ws.bind(wsbind)
    wsw = True
    print ("Listening Host '" + whostip + "' Port '" + str(wport) + "' ...")
    print ("++++++++++++++++++++++++++++++++")
    while wsw:
        try:
            ws_data = ws.recvfrom(10240)
            wstl = False
        except OSError:
            wstl = True
        if wstl:
            print("ERROR: Message too Long! Max type is 10240.")
            if os.name == "nt":
                print ("[OSError WinError 10040]:")
                os.system("net helpmsg 10040")
        else:
            ws_msg = ws_data[0]
            ws_addr = ws_data[1]
            ws_addr1 = ws_addr[0]
            ws_addr2 = ws_addr[1]
            if not int(ws_addr2) == wBport & str(ws_addr1):
                print("Blocked a Guest Message from " + str(ws_addr1) + ":" + str(ws_addr2))
            else:
                nt0 = datetime.datetime.now()
                nowtime = nt0.strftime('%Y/%m/%d %H:%M:%S')
                if ws_msg.decode("utf_8") == "/q":
                    wsw = False
                    print (nowtime + " - " + str(ws_addr1) + ":" + 
                    str(ws_addr2) + " : " + ws_msg.decode("utf_8"))
                    print("Connect Closed.")
                    ws.close()
                    break
                else:
                    print (nowtime + " - " + str(ws_addr1) + ":" + 
                    str(ws_addr2) + " : " + ws_msg.decode("utf_8"))
    return 0


def wDef(wArgs):
    if not wArgs[0] == "launch":
        return 0
    print(str(wArgs[1]) + " - " + str(wArgs[2]))
    return 0