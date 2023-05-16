a = input()

b1 = a.split("+")
b2 = a.split("-")
b3 = a.split("*")
b4 = a.split("/")

if len(b1) == 2:
    print(int(b1[0])+int(b1[1]))
elif len(b2) == 2:
    print(int(b2[0])-int(b2[1]))
elif len(b3) == 2:
    print(int(b3[0])*int(b3[1]))
elif len(b4) == 2:
    print(int(b4[0])//int(b4[1]))
