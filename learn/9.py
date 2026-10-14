#类
#类中的函数属于方法 与函数规则相同
#可以通过实例访问的变量称为属性

class Dog:
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is siting")

    def roll(self):
        print(f"{self.name.title()} is rolling")

dog1 = Dog("aaa",5)
print(f"{dog1.name.title()}'s age is {dog1.age}")
dog1.sit()
dog1.roll()
#继承
class Wolf(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
mywolf = Wolf("bbb",13)
print(f"{mywolf.name.title()}'s age is {mywolf.age}")

#见9.1&9.4&9.6.py

#python标准库





