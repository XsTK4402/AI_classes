# #方法一

# number = input()
# list = number.split()

# # print(list)

# i = 0
# c = []

# while i < len(list):

#     b = int(list[i])
#     c.append(b+1)
#     # print(c)
#     i = i + 1

# list2 = " ".join(map(str, c))
# print(list2)


# #方法二
# a = input().split()
# b = [str(int(x)+1) for x in a]
# c = " ".join(b)
# print(c)


#方法三
print(" ".join([str(int(i) +1) for i in input().split()]))