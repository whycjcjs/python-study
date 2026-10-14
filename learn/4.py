print(end=" ")
for a in range(1,10):
    for b in range(1,10):
        if b<=a:
            print(b,"*",a,"=",a*b,end=" ")
    print("\n",end=" ")
#min() max() sum()
#range()作用
## **乘方
c=list(range(1,11))

d=[2**value for value in range(1,11)]
print(c)
print(d)
#use a part of the 数列（数组）
#d[2: ] d[ :2]
print(d[0:3])
e=d[0:3]
print(e)
#元组
f=(1,2,3)
for a in f:
    print(a)
f=(2,3,4)
for a in f:
    print(a)



