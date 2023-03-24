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
    global mainexit
    mainexit = 0
    
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
        mainexit = 1
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
    wsbindGet = whostip, wport
    wsbindSend = wBhostip, wBport
    wthArgs = ("launch", "114514")
    _thread.start_new_thread(wSend, wthArgs)
    _thread.start_new_thread(wGet, wthArgs)
    os.system ("title pyChat v0.1 by wyf9 2023.3.19 - Single Chat - Computer A")
    while mainexit == 0:
        pass
    return 0


def wSend(wArgs1, wArgs2):
    sleep(1)
    p_addr = (wBhostip, wBport)
    print("Allowed Partner host: " + str(wBhost) + " - IP: " + str(wBhostip) + " - Port: " + str(wBport) + ".")
    
    print ("Input /q to Stop Listen.")
    while True:
        try:
            q0 = wAPIgetChar.wMain()
            if q0 == "null":
                q0 = ""
            q1 = input("> " + q0)
            q = q0 + q1
            if q == "/q":
                mainexit = 1
                break
            qw = bytes(q, 'utf-8')
            ws.sendto(qw, p_addr)
            nt0 = datetime.datetime.now()
            nowtime = nt0.strftime('%Y/%m/%d %H:%M:%S')
            print (nowtime + " - You : " + q)
        except KeyboardInterrupt:
            print("Ctrl + C\nQuitting Program...")
            wl.acquire()
            mainexit = 1
            wl.release()
            ws.close()
            exit()
    
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
            print("ERROR: Message too Long! Max type is 10240.")
            if os.name == "nt":
                print ("[OSError WinError 10040]:")
                os.system("net helpmsg 10040")
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
                    print("Connect Closed.")
                    ws.close()
                    break
                else:
                    print (nowtime + " - " + str(ws_addr1) + ":" + 
                    str(ws_addr2) + " : " + ws_msg.decode("utf_8"))
    return 0