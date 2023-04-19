from encodings import utf_8
utf_8
import os
import sys
from Sources import wAPIgetChar
from Sources import SingleChat
from Sources import LG
from Sources import Hello
from Sources import wAPICheckLib


def pyChat():
    
    os.system("title pyChat v0.1 by wyf9 2023.3.18")
    
    print ("pyChat 主菜单")
    print ("a / 1. 启动一个服务器")
    print ("b / 2. 加入一个服务器")
    print ("c / 3. 私聊")
    print ("g / 9. 这个程序内置小游戏??")
    print ("q / e / 0. 退出")
    print ("\n")

    while True: 
        wChar = wAPIgetChar.wMain()

        match wChar:

            case "a" | "1":
                print ("Server Mode Not Available.")

            case "b" | "2":
                print ("Console Mode Not Available.")

            case "c" | "3":
                print ("================================")
                print ("私聊模式")
                SingleChat.wMain()
                print ("================================")

            case "g" | "9":
                print ("================================")
                LG.wMain()
                print ("================================")

            case "q" | "0" | "e":
                print ("================================")
                print ("正在退出...")
                os.system("title  ")
                return 0
            
            case "w" | " " | "h":
                Hello.wMain()

    return 0



if __name__ == "__main__":
#    cln = False
#    cl =  wAPICheckLib.wMain("urwid", "./Sources/lib/urwid212.tar.gz", "https://wyf01239.github.io/webget/pyChat/lib/urwid212.tar.gz", False)
#       if cl != 0:
#            print("pyChat 启动失败.")
#            exit(1)
#        else:
#            cln = True
#            if cln != False:
#                if os.system("python Main.py") != 0:
#                    print("请重新启动 CmdAdmin.")
#                    exit(-1)
    match sys.argv[1:]:
        case ["/Server"]:
            print ("OK")
        case _:
            pyChat()