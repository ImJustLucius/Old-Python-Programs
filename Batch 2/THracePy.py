#Jonathan M Lucius
#This program simulates the race between 'the tort and the hare'
import random

def tort_move(pos):
    rng = random.randint(1,10)
    if(rng<=5):
        pos+=3
    elif(rng<=7):
        pos-=5
    else:
        pos+=1
    
    return pos

def hare_move(pos):
    rng = random.randint(1,10)
    if(rng<=2):
        pos = pos
    elif(rng<=4):
        pos+=7
    elif(rng==5):
        pos-=10
    elif(rng<=8):
        pos+=1
    else:
        pos-=2
    
    return pos
        
time = 0        
tort = 1        
hare = 1

while(tort<50 and hare<50):

    tort = tort_move(tort)

    if(tort<1):
        tort = 1
    
    hare = hare_move(hare)
    
    if(hare<1):
        hare = 1

    if(tort>hare):
        print(' '*(hare-1),'H',' '*((tort-hare)-1),'T',' '*(50-tort))
    elif(hare>tort):
        print(' '*(tort-1),'T',' '*((hare-tort)-1),'H',' '*(50-hare))
    else:
        print(' '*(tort-1),'OW!!',' '*(50-tort))
    
    time+=1

if tort >= hare: winner = 'Tortoise!!!'
else: winner = 'Hare...'

print(f'And after {time} seconds, the winner is... {winner}')

End = input('Press enter to exit...')