def my_map(fn, items):
    rtn=[]
    for x in items:
        rtn.append(x)
    return rtn


a = [1,2,3,4]
b = my_map(str,a)
print(b)

a = 1,2,3,4
b = map(str,a)
print(list(b))