lottery = set()

import random

a = random.randint(1,48)
print(a)
print(len(lottery))

while len(lottery) <= 6:
    lottery.add(a)

print(lottery)