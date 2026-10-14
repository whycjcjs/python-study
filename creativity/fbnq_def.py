a = int(input())
b = [1,1]
num=2
while num < a:
    b.append(b[num-1]+b[num-2])
    num += 1
print(b[a-1])

c = int(input())
d = [1,1]
def f(n):
    if n==1 or n==2:
        return 1;
    else:
        return f(n-2) + f(n-1)

print(f(c))

