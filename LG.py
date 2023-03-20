from encodings import utf_8
import random

while int(Over) < 26:
  Over=input('输入最高值 (大于25): ')

UN=input('请输入你的数字：')
SN=random.random(1,Over)

#判定
while int(UN) < int(SN):
  print('666')
  input('按回车可以继续  :]')
  print(':(((((((((')
  print(SN + '才是对的')
  input('按回车重试')
