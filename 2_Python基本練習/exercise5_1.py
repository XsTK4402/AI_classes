a = input()
b = a[::-1]

c= []

for x in b:
    if x not in c:
        c.append(x)
    else:
        continue

d = c[::-1]
e = ''.join(d)

print(e)
