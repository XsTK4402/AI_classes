a = input()
a_split_letter = a[0]
a_split_numbers = a[1:9]
a_split_lastnum = a[-1]

c = 0

if a_split_letter == "A":
    c = 1 + (0*9)
if a_split_letter == "B":
    c = 1 + (1*9)
if a_split_letter == "C":
    c = 1 + (2*9)
if a_split_letter == "D":
    c = 1 + (3*9)
if a_split_letter == "E":
    c = 1 + (4*9)
if a_split_letter == "F":
    c = 1 + (5*9)
if a_split_letter == "G":
    c = 1 + (6*9)
if a_split_letter == "H":
    c = 1 + (7*9)
if a_split_letter == "I":
    c = 3 + (4*9)
if a_split_letter == "J":
    c = 1 + (8*9)
if a_split_letter == "K":
    c = 1 + (9*9)
if a_split_letter == "L":
    c = 2 + (0*9)
if a_split_letter == "M":
    c = 2 + (1*9)
if a_split_letter == "N":
    c = 2 + (2*9)
if a_split_letter == "O":
    c = 3 + (5*9)
if a_split_letter == "P":
    c = 2 + (3*9)
if a_split_letter == "Q":
    c = 2 + (4*9)
if a_split_letter == "R":
    c = 2 + (5*9)
if a_split_letter == "S":
    c = 0 + (6*9)
if a_split_letter == "T":
    c = 2 + (7*9)
if a_split_letter == "U":
    c = 2 + (8*9)
if a_split_letter == "V":
    c = 2 + (9*9)
if a_split_letter == "W":
    c = 3 + (2*9)
if a_split_letter == "X":
    c = 3 + (0*9)
if a_split_letter == "Y":
    c = 3 + (1*9)
if a_split_letter == "Z":
    c = 3 + (3*9)

d = 0

for i in range(len(a_split_numbers)):
    d = int(a_split_numbers[i]) * (len(a_split_numbers) - i) + d

e = int(a_split_lastnum)

check = c + d + e

if check % 10 == 0:
    print("合法")
else:
    print("不合法")
