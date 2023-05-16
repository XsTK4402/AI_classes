year = int(input())

normal_year = True

if year % 4 != 0:
    normal_year = True
elif year % 4 == 0 and year % 100 != 0:
    normal_year = False
elif year % 100 == 0 and year % 400 != 0:
    normal_year = True
else:
    normal_year = False

if normal_year == True:
    print("False")
else:
    print("True")
