a = input("please input a number and I will print it point three\n")
print(a)
b="hello"
b += "\nI'm why i'm handsome"
print(b)
a = int(a)
print(a+3)

c = input("What kind of cake do you want?\n")
if c[0] == "a" or c[0] == "e" or c[0] == "i" or c[0] == "o" or c[0] == "u":
    print(f"You want to get an {c}!")
else:
    print(f"You want to get a {c}!")

print("I will ask if you love me until you say you love me")
print("you just need to say 'love'")
massage = " "
while massage != "love":
    massage = input("answer me please? I'm a boy who love you very much!")
    if massage == "love":
        print("yeah~ I love you very much!")
    else:
        print(massage)
# the notice continue break is same as cpp so i won't write them again
z = 0
y = True
x={}
while y:
    z+=1
    name = input("what is your name?")
    love = input("what is your love?")
    x[name] = love
    w = input("are there next one? \n please answer 'yes'")
    if w != "yes":
        y=0
for key,value in x.items():
    print(key,"love",value)
#用while 处理列表和字典
