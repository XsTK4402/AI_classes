num = int(input())
c = []
c.append(num)

while num >= 1:
    if num % 2 == 0:
        num = num/2
        c.append(num)
    else:
        num = num - 1
        c.append(num)

print(len(c)-1)