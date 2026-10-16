from random import randint

def guessnumber1():
    teb = '1'
    while teb == '1':
        t = int(input("what scope of number do you want to guess. 1 to ? \n"))
        print("I thought a number,please try to guess it")
        a = randint(1, t)
        while True:
            b = int(input("\n"))
            if b == a:
                print("bingo,you are smart")
                break
            elif b > a:
                print("big")
            else:
                print("small")
        teb = input("do you want to play again?please answer '1' or '0'\n")

def guessnumber2():
    teb1 = '1'
    while teb1 == '1':
        t1 = int(input("你想猜数的范围是1到多少\n"))
        print("我想到了一个数字,尝试猜一猜")
        a1 = randint(1, t1)
        while True:
            b1 = int(input("\n"))
            if b1 == a1:
                print("对了,你好聪明")
                break
            elif b1 > a1:
                print("大了")
            else:
                print("小了")
        teb1 = input("你想继续玩吗\n‘1’继续 \n‘0’退出\n")

c = input("what language do you want. 'c' as chinese \n and 'e' as english \n")
A=c.isdigit()
while int(A-1) != -1:
    c=input("answer wrong please answer again\n")
    A = c.isdigit()
while c != 'e' and c != 'c':
    c=input("answer wrong please answer again\n")

if c == 'e':
    guessnumber1()
elif c == "c":
    guessnumber2()