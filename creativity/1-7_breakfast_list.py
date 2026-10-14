import time
print("-------------------------------")
print("------------CANTEEN------------")
print("-we need you provide some date-")
print("--------1 is baozi 2yuan-------")
print("------2 is hunudun 10yuan------")
print("------3 is youtiao 2yuan-------")
print("-------------------------------")
breakfast={}
studentnum={}
studentmoney={}
num=0
classnum = input("How many class are here?\n")
A=classnum.isdigit()
while int(A-1) == -1:
    classnum=input("answer wrong please answer again\n")
    A = classnum.isdigit()

while num < int(classnum):
    if int(num) == 0:
        print("Now the first class")
    if num != 0:
        print("--------------------------")
        print("Ok the next class")
    num += 1
    F= True
    snum = 0
    breakfast2 = {}
    while F:
        money=0
        breakfast1 = []
        snum+=1
        name = input("What your name?\n")

        while name.isdigit():
            name = input("Please input your true name\n")

        while True:
            breakfast3 = input("What kind of breakfast do you want?\n")
            B = breakfast3.isdigit()
            while int(B - 1) == -1:
                breakfast3 = input("answer wrong please answer again\n")
                B = breakfast3.isdigit()
            while breakfast3 != "1" and breakfast3 != "2" and breakfast3 != "3":
                breakfast3 = input("we only have breakfast 1 2 3 please answer again\n")
            if breakfast3 == "1":
                money += 2
            elif breakfast3 == "2":
                money += 10
            else:
                money += 2
            breakfast1.append(breakfast3)
            FF = input("Are you need other? answer 'y' or 'n'?\n")
            while FF != 'y' and FF != 'n':
                FF = input("answer wrong please answer again\n")
            if FF == "n":
                break
        breakfast2[name]= breakfast1

        string = input("Are there any student behind you? answer 'y' or 'n'?\n")
        while string != 'y' and string != 'n':
            string = input("answer wrong please answer again\n")
        if string == "n":
            F= False
        studentmoney[(num,name)] = money
    studentnum[num] = snum
    breakfast[num]=breakfast2

for key,value in breakfast.items():
    print(f"class{key} ",end = "")
    if studentnum[key] != 1:
        print(f"have {studentnum[key]} students in this class")
    else:
        print(f"have {studentnum[key]} student in this class")
    for key1,value1 in value.items():
        print(f"{key1} need",end = " ")
        baozi1 = 0
        hundun1 = 0
        youtiao1 = 0

        for food in value1:
            if int(food) == 1:
                baozi1 += 1
            elif int(food) == 2:
                hundun1 +=1
            else:
                youtiao1 +=1

        print(f"youtiao*{youtiao1} baozi*{baozi1} hundun*{hundun1}",end=" ")
        print(f"and {key1} need to pay {studentmoney[(key,key1)]} yuan")
#The end
time.sleep(10)