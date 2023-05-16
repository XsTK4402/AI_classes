a = int(input())
i = 1

while i <= a:
    print("*"*i)
    i = i+1

a = int(input())
i = 2
c = []
d = []

while i <= (a**0.5):
    if a % i == 0:
        c.append(i)
        i = i+1
    else:
        d.append(i)
        i = i+1

print(c)
print(d)

if not c:
    print(a)
