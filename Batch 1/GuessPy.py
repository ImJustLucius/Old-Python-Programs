#Jonathan M Lucius
#This script will have the user try to guess a chosen number in the range of 1-100 
import random

def att():
    attempt = int(input("Guess the number that's between 1-100 (inclusive): "))
    while(attempt>100 or attempt<1):
        print('Not with the range!')
        attempt = int(input("Guess the number that's between 1-100 (inclusive): "))

    return attempt

num = random.randint(1,100)
# num = 52

guesses = 0
status = 'lost'

while(guesses<10):

    guess = att()
    guesses+=1

    if(guess == num):
        print(f'You got it! Took you {guesses} tries!')
        status = 'won'
        break
    elif(guess>num):
        print('Too High...')
    elif(guess<num):
        print('Too Low...')


if(status=='lost'):
    print(f'You are out of tries! The number was: {num}\nBetter luck next time!')