print('This temperature conversion program converts other temperature types to Farenheit')
print('The temperature types are\n')
print('C - Celcius')
print('K - Kelvin')
print('N - Newton')
print('X - eXit\n')
print('To use the converter you must input a value and one of the temperature types.')
print('For example 32 C converts 32 degrees from Celsius to Fahrenheit\n')

def C2F(v) :
    f = (v * 9 / 5) + 32
    return f

def K2F(v) :
    c = v - 273.15
    f = C2F(c)
    return f

def N2F(v) :
    f = v*5.4545 + 32
    return f

value, function = input("Please enter a value and it's type to be converted ").split(" ")
value = float(value)
function = function.upper()

while function != 'X' :
    if function == 'C' :
        print(value, function, 'is ', C2F(value), 'in Fahrenheit')
    elif function == 'K' :
        print(value, function, 'is ', K2F(value), 'in Fahrenheit')
    elif function == 'N' :
        print(value, function, 'is ', N2F(value), 'in Fahrenheit')
    value, function = input("Please enter a value and it's type to be converted ").split(" ")
    value = float(value)
    function = function.upper()

print('Thanks for using the temperature converter')
