import random

random.seed()

int sumEven = 0
int sumOdd = 0

for i in range(0, 20) :
  x = random.randint(1, 100)
  if x % 2 == 0:
    sumEven += x
  else:
    sumOdd += x
    
print('even: ', sumEven)
print('odd: ', sumOdd)
