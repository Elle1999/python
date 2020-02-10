import math

print('This calculator requires you to enter a function and a number')
print('The functions are as follows:')
print('S - sine')
print('C - cosine')
print('T - tangent')
print('R - square root')
print('N - natural log')
print('X 0- eXit the program')

f, v = input("Please enter a function and a value ").split(" ")
v = float(v)
while f != 'X' and f != 'x':
    if f == 'S' or f == 's' :
        calculation = math.sin(v)
        print('The sine of your number is ', calculation)
    elif f == 'C' or f == 'c' :
        calculation  = math.cos(v)
        print('The cosine of your number is ', calculation)
    elif f == 'T' or f == 't' :
        calculation =  math.tan(v)
        print('The tangent of your number is ', calculation)
    elif f == 'R' or f == 'r' :
        calculation = math.sqrt(v)
        print('The square root of your number is ', calculation)
    elif f == 'N' or f == 'n' :
        calculation = math.log10(v)
    elif f == 'X' or f == 'x' :
        print('Thanks for using the calculator')
    
    if f != 'X' and f != 'x':
       f, v = input("Please enter a function and a value ").split(" ")
       v = float(v)

print('Thanks for using the calculator')
