n = int(input())

while n >= 2:
    is_prime = True
    i = 2
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i = i+1

    if is_prime:
        print(n)
        break

    n = n-1

#-------------------------------------------------------------------
def is_prime_number(n: int) -> bool:
    "判斷是否為質數"
    if n == 2:
        return True
    
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True