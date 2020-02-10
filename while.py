import random

random.seed()
count = 1
guess = int(input('Guess a number between 1 and 10\n'))
answer = 'y'

num = random.randint(1, 10)
while(answer == 'y') :
    while(guess != num) :
        guess = int(input('Guess a number between 1 and 10\n'))
        count +=1

    print('It took', count, 'guesses to guess', num)
    answer = input('Would you like to play again? y for yes, n for no\n')
    if answer == 'y' :
      num = random.randint(1, 10)
      guess = int(input('Guess a number between 1 and 10\n'))
      count = 1

print('goodbye')
