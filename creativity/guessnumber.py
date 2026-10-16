from random import randint
c= input("what language do you want. 'c' as chinese \n and 'e' as english \n")
if c == 'e':
    teb = '1'
    while teb == '1':
        t = int(input("what scope of number do you want to guess. 1 to ? \n"))
        print("I thought a number,please try to guess it")
        a = random.randint(1 , t)
        while True:
            b = int(input ("\n"))
            if b == a:
                print("bingo,you are smart")
                break
            elif b > a:
                print("big")
            else:
                print("small")
        teb =input("do you want to play again?please answer '1' or '0'\n")
else:
    teb = '1'
    while teb == '1':
        t = int(input("你想猜数的范围是1到多少\n"))
        print("我想到了一个数字,尝试猜一猜")
        a = random.randint(1 , t)
        while True:
            b = int(input ("\n"))
            if b == a:
                print("对了,你好聪明")
                break
            elif b > a:
                print("大了")
            else:
                print("小了")
        teb =input("你想继续玩吗\n‘1’继续 \n‘0’退出\n")