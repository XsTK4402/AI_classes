# a = input()
# b = a.split(",")

# list1 = b[0]
# list2 = b[1]

# str_list1 = list1.split()
# int_list1 = list(map(int, str_list1))
# str_list2 = list2.split()
# int_list2 = list(map(int, str_list2))


# c = []
# i = 0

# while i < len(int_list1):
#     # 遍歷 list2 中的每個元素
#     j = 0
#     while j < len(int_list2):
#         # 如果兩個元素相同，就加入到 common_values 中
#         if int_list1[i] == int_list2[j]:
#             c.append(int_list1[i])
#         j += 1
#     i += 1

# if len(c) == 3:
#     print(100)
# elif len(c) == 4:
#     print(1000)
# elif len(c) == 5:
#     print(10000)
# else:
#     print(0)

#--------------------------------------------------------------

a = input()
b = a.split(",")

c1 = b[0].split()
c2 = b[1].split()

d1 = set(map(int, (c1)))
d2 = set(map(int, (c2)))

e = d1 & d2
print(e)

if len(e) == 3:
    print(100)
elif len(e) == 4:
    print(1000)
elif len(e) == 5:
    print(10000)
else:
    print(0)