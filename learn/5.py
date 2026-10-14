import math

a=[1,2,3,4,5]
if a[0]==1:
    print("True")
if 1 in a:
    print("True")
# == != >= <=
#and or
b=True
c=False
if  (1 in a) == b:
    if  (1 in a) != c:
        print(b)
if a[1]==2:
    d=0
elif a[2]==2:
    d=1
else:
    d=2
print(d+1)

# round()四舍五入 a//b得到整数  int()舍弃小数

print("\n\n")
num=[]
z=0
for i in range(2,31):
    z=0
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            num.append(True)
            z=1
            break
    if z == 0:
        num.append(False)
for i in range(0,29):
    if num[i] == 0:
        print(i+2)
