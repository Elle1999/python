import random
import math

def fillList(count) :
    list = []
    for i in range(0, count) :
        list.append(random.randint(0,10))
    return list

def printList(lst) :
    for val in lst:
        print(val)

def sumList(lst) :
    sum = 0
    for val in lst:
        sum += val
    return sum

myList = fillList(25)

printList(myList)

numSum = sumList(myList)

print(numSum)
