from encodings import utf_8
utf_8
import random
from Sources import w114514

def wMain():
# 设定最高值
    MAX = 0
    a114 = 0
    print("输入 /q 结束游戏")
    while int(MAX) < 16:
        MAX=input('输入最高值 (大于 15 的整数): ')
        if MAX == "/q":
            print ("已退出游戏。")
            return 0
        try:
            if int(MAX) == int(114514):
                pass
        except:
            print("ERROR: 非法的数字 - NaN\n请重新输入。")
            MAX = 0
            continue
        if int(MAX) < 16:
            print('你就真心不按照提示来输入吗？！！！！')
            a114 = a114 + 1
            if a114 > 4:
                w114514.wMain()
            print("ERROR: 数字太小了, 请重新输入。")

    go = True
    UN = 0
    Att = 0
    SN=random.randint(1, int(MAX))
    
    # 判定
    
    while go == True:
        try:
            if UN == "/q":
                print ("已退出游戏。")
                go = False
                break
            elif int(UN) == 0:
                pass 
        except:
            print("ERROR: 非法的数字 - NaN, 请重新输入。")
            UN = "0"
            continue
        if int(UN) == 0:
            Att += 1
            UN=input('请输入你的数: ')
            
            if UN == "/q":
                print ("已退出游戏。")
                go = False
                break
        elif int(UN) < int(SN):
            UN=input('数字小了\n请输入你的数字: ')
            Att += 1
            if UN == "/q":
                print("已退出游戏。")
                return 0
        elif int(UN) > int(SN):
            Att += 1
            UN=input('数字大了\n请输入你的数字: ')
            
            if UN == "/q":
                print("已退出游戏。")
                return 0
        elif int(UN) == int(SN):
            UN=input('NICE! 你猜对了! 数字就是: ' + str(SN) +  '\n你猜了' + str(Att) + '次！\n按回车继续...\n')
            go = False
            break
        else:
            print("Dead ERROR: Unknown Error. :(((((((((")
            print("已退出游戏。")
            go = False
            break
    return 0
# √  :)
# ( ͡° ͜ʖ ͡°)