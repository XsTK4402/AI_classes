a = input()
b = a.split()
print(b)

c = []
for x in b:
    c.append(x[::-1])

print(c)