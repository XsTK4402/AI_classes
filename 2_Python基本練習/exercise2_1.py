a = input()
b = a.split()
c= int(b[0])
d= int(b[1])

i = 1

while i <= c:
    k = 1
    while k <= d:
        print(f'{i}x{k}={i*k}')

        k = k+1
    i = i+1