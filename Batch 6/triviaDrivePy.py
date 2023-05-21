#Jonathan M Lucius
#The purpose of this code is to act as a the main module for the Trivia game.
import triviaFuncPy
import triviaClassPy

qList = triviaFuncPy.TriviaTime()

y = 0
p1 = 0
p2 = 0

for x in qList:
    
    if(y%2==0):
        print('Player 1, answer this question:\n')
    else:
        print('Player 2, answer this question:\n')
    
    print(x,'\n')
    
    ans = int(input('Your answer (Choose a number): '))

    truth = x.get_ans()
    
    #print(f'Truth is {type(truth)}, ')
    
    if(ans==truth):
        print('Correct! +1 point to you!')
        if(y%2==0):
            p1+=1
        else:
            p2+=1
    else:
        print(f'Wrong, The correct answer was number {truth}')

    y+=1

winner = 1 if p1>p2 else 2


print(f'And the winner is... Player {winner}!!!') if p1!=p2 else \
    print('And the winner is... No one! its a tie!')

print(f'The scores are... Player 1 - {p1} PLayer 2 - {p2}')