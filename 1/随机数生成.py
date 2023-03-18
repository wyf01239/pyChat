from encodings import utf_8
utf_8

#生成随机数
seed = 325
def random(): 
    global seed 
    seed = seed ** 2 
    return int(str(seed)[1:5])

U_R_S_number = input('请输入你的数字：')


SYS_num = random()


if int(U_R_S_number) == int(SYS_num):
    print('666')
else:
    print(':(((((((((')
    print(SYS_num+' 才是对的')

