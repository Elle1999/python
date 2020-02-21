import random

def createList(count) :
    list = []
    for i in range(0, count) :
        list.append(random.randint(1,100))
    return list

def printList(lst) :
    for val in lst:
        print(val)

def smallLarge(lst) :
    smallest = lst[0]
    largest = lst[0]
    for val in lst:
        if smallest > val :
            smallest = val
        if largest < val :
            largest = val
    return smallest, largest

newlist = createList(25)
printList(newlist)
s, l = smallLarge(newlist)

print('The smallest number is ', s, 'The largest number is ', l)
