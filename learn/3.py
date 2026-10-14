import time
import os
a=[1,3,2,6,5,4]
b=["b","a","c","d","g","f","e"]
print (a[0]," 123 ",b[0])
a[0]=0
c=f"{a[0]}  123  {b[0]}"
print (c)
b.append("h")
print(b[7])
a.insert(3,3.5)
print(a)
del  a[3]
print(a)
d=a.pop(1)
print(a)
print(d)
#we can get the numerical value when using pop()
#but we can't when using del x
e="h"
b.remove(e)
print(b)
print(e)
#remove() is similar to pop() but there is a few different
a.sort()
print(a)
print(sorted(b))
print(b)
b.reverse()
print(b)
f=len(b)
print(f)
print(b[-1])
time.sleep(10)
