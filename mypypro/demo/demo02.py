import random
import math


for i in range(5):
    value = random.randint(1, 6)
    print(value)

num = 10

print(math.sqrt(num))


def print_num(x):
    for i in range(x):
        print(i)
        return

    
print_num(10)
