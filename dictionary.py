import random
import math

assoc = {'up' : 'down', 'in': 'out', 'front':'back'}
update = {'sad' : 'happy', 'off': 'on', 'wet' : 'dry', 'boy' : 'girl', 'sunny' : 'cloudy'}

assoc.update(update)

print('Word association game. I will say a word and you say what comes to mind.')
count = 0

for word in assoc :
    print(word)
    answer = input('Enter association\n')
    if(answer == assoc[word]) :
        count+=1
print('You associated', count, 'out of', len(assoc), sep = ' ')
