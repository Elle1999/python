import random
import math

def print2D(list) :
    for row in range(0, 4) :
        for col in range(0, 3) :
            print(list[row][col], end = ' ')
        print(' ')
    return

def sum2D(list) :
    count = 0
    for row in range(0, 4) :
        for col in range(0, 3) :
            if list[row][col] % 2 == 0 :
                count += 1
    return count

list = [[random.randint(0, 25) for x in range(3)] for y in range(4)]
print2D(list)
evens = sum2D(list)

print(evens)
