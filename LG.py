from encodings import utf_8
utf_8
import random
import wAPIgetChar

def wMain():
    # 设定最高值
    while int(Over) < 26:
        Over=input('输入最高值 (大于25): ')

    print("输入 /q 结束游戏")
    UN=input('请输入你的数: ')
    SN=random.random(1,Over)

    # 判定
    while True:
        if int(UN) < int(SN):
            UN=input('数字小了\n请输入你的数字: ')
        elif int(UN) > int(SN):
            UN=input('数字大了\n请输入你的数字: ')
        elif int(UN) == int(SN):
            UN=input('你猜对了! 数字就是: ' + SN + '.\n按q退出, 按其他键重来')
            choose = wAPIgetChar.wMain()
        else:
            print("ERROR: Unknown Error. :(((((((((")


# √