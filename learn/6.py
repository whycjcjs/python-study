from binascii import a2b_base64

a={"3":5,'a':'b','2':"a"}
print(a["3"],a["a"],a["2"])
# like map in cpp
a[91]=78
print(a)
# or a={}
del a[91]
print(a)
print(a.get(91,"世界上根本就没有这种键值"))

for key,value in a.items():
    print(key," ",value)
for tt in a.keys():
    print(tt,end=" ")
for tt in sorted(a.keys()):
    print(tt,end=" ")
print("\n")
for tt in a.values():
    print(tt)

x = {1:"a",2:"b",3:"c"}
y = {4:"d",5:"e",6:"f"}
z = {7:"g",8:"h",9:"i"}
xvz = [x,y,z]
#字典中可以存储列表 列表中可以存储字典 字典中可以嵌套字典


grades = {
    "27":[1,2,3],
    "28":[4,5,6],
    "29":[7,8,9]
}
breakfast = {
    "27": {"1":"a","2":"b","3":"c"},
    "28": {"1":"b","2":"a","3":"b"},
    "29": {"2":"a","3":"a","4":"c"}
}
motion_lists= [
    {"1":"tt","2":"ff","3":"jj"},
    {"1":"tt","5":"ff","6":"jj"},
    {"7":"tt","1":"ff","9":"jj"},
]

for a in motion_lists:
    print(a["1"])
for a in grades.values():
    print(a)
for a in breakfast.values():
    print(a.get("1","世界上根本就没有这种键值"))
