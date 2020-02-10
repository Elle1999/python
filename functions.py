def getValue() :
    val = int(input('Enter a number'))
    return val
def cubeIt(val) :
    return val * val * val
def sumIt() :
    return getValue() + getValue() + getValue()

x = getValue()
print('The cube of the value is ', cubeIt(x))
sum_values = sumIt()
print('The sum of three values is', )
