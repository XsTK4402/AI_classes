a = input()
b = a.split()

print(b)

if int(b[0]) <= int(b[1]):
    print(int(b[1]) - int(b[0]))

if int(b[0]) > int(b[1]):
    print(200 + int(b[1]) - int(b[0]))
