import random

random.seed()
count = 1
points = 10
valid = 0
while(valid == 0) :
    guess = int(input('Guess a number between 1 and 10\n'))
    if guess <=10 and guess >=1 :
        valid = 1
    else:
        print('Invalid number. Try again')

valid = 0

num = random.randint(1, 10)

while(guess != num) :
   while(valid == 0) :
    guess = int(input('Guess a number between 1 and 10\n'))
    if guess <=10 and guess >=1 :
        valid = 1
    else:
        print('Invalid number. Try again')
   valid = 0
   count +=1
   points -=2

print('It took', count, 'guesses to guess', num , 'your score is ', points)

