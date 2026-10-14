def abc():
    """what?"""
    print("Welcome to python")
abc()

def abd(a1,b1,c1):
    """what?"""
    print(a1,b1,c1,sep="",end="")

for i in range(1,3):
    a = input()
    b = input()
    c = input()
    abd(a,b,c)
#形参 实参 关键字实参 可以给形参一个初始的值

def bb(name1,sex1="boy"):
    """Just an example"""
    print(f"{name1} is a {sex1}")
name = input("What's your name")
sex = input("What's your sex answer 'boy' or 'girl'")
bb(name1=name,sex1=sex)

#函数返回值
def tt(first_name1,last_name1):
    allname=f"{first_name1} {last_name1}"
    return allname
print(tt("W","hy"))

 #返回值可以是一个字典

#可以传递列表
ze = []
def ta(nam):
    while nam:
        ze.append(nam.pop(0))
    for aab in ze:
        print(aab)
tze = ["why","why1","why2"]
ta(tze[:])
print(tze)

#传递任意数量的实参 *project

def ata(*aaa):
    for aab in aaa:
        print(aab)
ata("why")
ata("why","why1","why2")

#位置实参 和 数量实参可以同时传输

#*是元组 **是字典

#模块化






