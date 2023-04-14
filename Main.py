from encodings import utf_8
utf_8
import os
import sys
from Sources import wAPIgetChar
from Sources import SingleChat
from Sources import LG
from Sources import Hello
from importlib import import_module


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

def CheckLib(wname, wfile, wurl):
    wErr = False
    # wname: str, 名称
    # wfile: str, 本地安装文件（whl / tar.gz) 地址, 格式详见往下 7 行
    # wurl: str, 自定义安装文件下载地址
    try:
        import_module (wname)
    except:
        print("未安装库 " + wname + ", 正在启动安装")
        # 格式: "./xxx/xxx/xxx.tar.gz" or "./xxx/xxx/xxx.whl"
        wret = os.system("python -m pip install " + wfile)
        if wret != 0:
            wErr = True
        else:
            print("成功安装库 " + wname)
    if wErr == True:
        print(wname + " 安装失败, 请自行安装库: https://pypi.org/project/" + wname + " 或 " + wurl)
        return 1
    else:
        return 0

if __name__ == "__main__":
    if CheckLib("urwid", "./Sources/lib/urwid212.tar.gz", "https://wyf01239.github.io/webget/pyChat/lib/urwid212.tar.gz") != 0: exit(1)
    match sys.argv[1:]:
        case ["/Server"]:
            print ("OK")
        case _:
            pyChat()