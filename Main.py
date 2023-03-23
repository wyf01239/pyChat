from encodings import utf_8
utf_8
import os
from Sources import wAPIgetChar
from Sources import SingleChat
from Sources import LG
from Sources import Hallo

def pyChat():
    
    try:
        os.mkdir("data")
    except FileExistsError:
        pass
    except:
        print("ERROR: Create data Dir Failed.")
        return 0
    
    os.system("title pyChat v0.1 by wyf9 2023.3.18")
    
    print ("pyChat Main Menu")
    print ("a / 1. Start a Server")
    print ("b / 2. Join a Server")
    print ("c / 3. Single Chat")
    print ("g / 9. Little Game??")
    print ("q / e / 0. Quit")
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
                print ("Single Chat Mode")
                SingleChat.wMain()
                print ("================================")

            case "g" | "9":
                print ("================================")
                LG.wMain()
                print ("================================")

            case "q" | "0" | "e":
                print ("================================")
                print ("Quitting Program...")
                break
            
            case "w" | " " | "h":
                Hallo.wMain()

    os.system("title       ")
    return 0

if __name__ == "__main__":
    pyChat()