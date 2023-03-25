from encodings import utf_8
utf_8
import socket
import os
import datetime
import _thread
import threading
from time import sleep
from Sources import wAPIgetChar

ws = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
wl = threading.Lock()

def wMain():
    global whostip
    global wBhost
    global wBhostip
    global wBport
    global wport
    global wsbindGet
    global wsbindSend
    global wthArgs
    global wExit
    
    os.system ("title pyChat v0.1 by wyf9 2023.3.19 - Single Chat - Computer A")
    print ("Your HostName: " + socket.gethostname())
    whostip = socket.gethostbyname(socket.gethostname())
    print ("Your Host IP: " + whostip)
    wport0 = input ("Input Your Port: 92__\n>>")
    wBhost = input ("Input Partner Host: ")
    try:
        wBhostip = socket.gethostbyname(wBhost)
    except:
        print("Unknown host!")
        return 0
    wBport0 = input("Input Partner Port: 91__\n>>")
    try:
        wBport1 = str(91) + wBport0
        wBport = int(wBport1)
    except ValueError:
        print("ERROR: Input Not a Port")
        return 0
    try:
        wport1 = str(92) + str(wport0)
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
    wExit = 0
    wsbindGet = whostip, wport
    wsbindSend = wBhostip, wBport
    wthArgs = ("launch", "114514")
    _thread.start_new_thread(wSend, wthArgs)
    _thread.start_new_thread(wGet, wthArgs)
    os.system ("title pyChat v0.1 by wyf9 2023.3.19 - Single Chat - Computer A")
    while True:
        if wExit == 1:
            input()
    return 0


def wSend(wArgs1, wArgs2):
    sleep(0.5)
    p_addr = (wBhostip, wBport)
    print("Allowed Partner host: " + str(wBhost) + " - IP: " + str(wBhostip) + " - Port: " + str(wBport) + ".")
    print ("Press any key to input.")
    print ("Press q to Stop Listen.")
    while True:
        try:
            q0 = wAPIgetChar.wMain()
            match q0:
                case "q":
                    qw = bytes("/q", 'utf-8')
                    ws.sendto(qw, p_addr)
                    wExit = 1
                    ws.close()
                    print("Now you can quit.")
                    while True:
                        input()
                case _:
                    q = input("> ")
                    if q == "/q":
                        qw = bytes("/q", 'utf-8')
                        ws.sendto(qw, p_addr)
                        wExit = 1
                        ws.close()
                        print("Now you can quit.")
                        while True:
                            input()
                    qw = bytes(q, 'utf-8')
                    try:
                        ws.sendto(qw, p_addr)
                        nt0 = datetime.datetime.now()
                        nowtime = nt0.strftime('%Y/%m/%d %H:%M:%S')
                        print (nowtime + " - You : " + q)
                    except OSError:
                        if wExit == 1:
                            while True:
                                input()
                        print ("Unknown Error.")
        except KeyboardInterrupt:
            print("Ctrl + C")
            wExit = 1
            ws.close()
            print("Now you can quit.")
            while True:
                input()
    
    return 0

def wGet(wArgs1, wArgs2):
    ws.bind(wsbindGet)
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
            if wExit == 0:
                print("Unknown Error")
            else:
                while True:
                    input()
        else:
            ws_msg = ws_data[0]
            ws_addr = ws_data[1]
            ws_addr1 = ws_addr[0]
            ws_addr2 = ws_addr[1]
            if not (str(ws_addr1), int(ws_addr2)) == (wBhostip, wBport):
                print("Blocked a Guest Message from " + str(ws_addr1) + ":" + str(ws_addr2))
            else:
                nt0 = datetime.datetime.now()
                nowtime = nt0.strftime('%Y/%m/%d %H:%M:%S')
                if ws_msg.decode("utf_8") == "/q":
                    wsw = False
                    print (nowtime + " - " + str(ws_addr1) + ":" + 
                    str(ws_addr2) + " : " + ws_msg.decode("utf_8"))
                    wExit = 1
                    ws.close()
                    print("Connect Closed.")
                    print("Now you can quit.")
                    while True:
                        input()
                else:
                    print (nowtime + " - " + str(ws_addr1) + ":" + 
                    str(ws_addr2) + " : " + ws_msg.decode("utf_8"))
    return 0
