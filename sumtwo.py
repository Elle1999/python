def sumTo(num1, num2) :
    if num1 > num2:
        small = num2
        large = num1
    else:
        small = num1
        large = num2
    sum = 0
    for i in range(small, large + 1) :
        sum += i
    return sum

input1 = int(input('Enter two numbers\n'))
input2 = int(input())
sumTwo = sumTo(input1, input2)
print(sumTwo)
