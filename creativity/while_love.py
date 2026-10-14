print("Hello and ee i want to ask you some questions")
print("I will ask if you love me until you say you love me")
print("if you gave me other answer then i will repeat you")
print("you just need to say 'love'")
massage = " "
while massage != "love":
    massage = input("answer me please? I love you very much!")
    if massage == "love":
        print("yeahhee~ I love you very much!")
    else:
        print(massage)