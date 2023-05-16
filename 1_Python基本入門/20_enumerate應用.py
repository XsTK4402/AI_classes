stds = ["1","2","3"]

for i,s in enumerate(stds,1):
    print(i,s)

a = [int(s)+1 for s in stds]
print(a)


# 把數字加進空集合(初學者)
b = []
for i in range(0,11):
    b.append(i)

print(b)

# 把數字加進空集合(進階)
c = [i for i in range(0,11)]
print(c)