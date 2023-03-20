from encodings import utf_8
utf_8
import random

def wMain():
    # 设定最高值
    Over = 0
    print("输入 /q 结束游戏")
    while int(Over) < 15:
        Over=input('输入最高值 (大于 15 的整数): ')
        if Over == "/q":
            print ("已退出游戏.")
            return 0
        try:
            if int(Over) == int(114514):
                pass
        except:
            print("ERROR: 非法的数字 - NaN\n请重新输入.")
            Over = 0
            continue
        if int(Over) < 15:
            print("ERROR: 数字太小了, 请重新输入.")

    SN=random.randint(1, int(Over))

    go = True
    UN = "0"
    # 判定
    
    while go == True:
        try:
            if UN == "/q":
                print ("已退出游戏.")
                go = False
                break
            elif int(UN) == 0:
                pass 
        except:
            print("ERROR: 非法的数字 - NaN, 请重新输入.")
            UN = "0"
            continue
        if int(UN) == 0:
            UN=input('请输入你的数: ')
            if UN == "/q":
                print ("已退出游戏.")
                go = False
                break
            elif int(UN) == 0:
                print("ERROR: 不能输入 0.")
        if int(UN) < int(SN):
            UN=input('数字小了\n请输入你的数字: ')
            if UN == "/q":
                print("已退出游戏.")
                return 0
            elif int(UN) == 0:
                print("ERROR: 不能输入 0.")
        elif int(UN) > int(SN):
            UN=input('数字大了\n请输入你的数字: ')
            if UN == "/q":
                print("已退出游戏.")
                return 0
            elif int(UN) == 0:
                print("ERROR: 不能输入 0.")
        elif int(UN) == int(SN):
            UN=input('你猜对了! 数字就是: ' + str(SN) + '. 按回车继续...')
            go = False
            break
        else:
            print("Dead ERROR: Unknown Error. :(((((((((")
            print("已退出游戏.")
            go = False
            break

# √

    return 0