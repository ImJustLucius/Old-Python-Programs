#Jonathan M Lucius
#The purpose of this program is to display the first x values of the chosen sequence
import math

def Fibseq(val):
    fibans = [0,1]
    for x in range(2,val):
        calc = fibans[x-2] + fibans[x-1]
        fibans.append(calc)
    return fibans

def Catfunc(pos):
    func = int((math.factorial(2*pos))/((math.factorial(pos+1))*(math.factorial(pos))))  #This is the Catalan sequence formula
    return func

def Catseq(val):
    catans = []
    for x in range(val):
        calc = Catfunc(x)
        catans.append(calc)
    return catans

def Lazyfunc(pos):
    func = int((pos**2 + pos + 2)/2)
    return func

def Lazyseq(val):
    Lazyans = []
    for x in range(val):
        calc = Lazyfunc(x)
        Lazyans.append(calc)
    return Lazyans

def Choices():
    print('1 - Fibonacci Sequence\n2 - Catalan Sequence\n3 - Lazy Caterer\'s Sequence')

loop = 'yes'

while(loop == 'yes' or loop == 'Yes'):
    Choices()
    
    choice = int(input('Please choose one of the options (1-3): '))

    while(choice<=0 or choice>3):
        choice = int(input('Out of bounds. Please re-enter (Range 1-3): '))

    pos = int(input('Please enter the number of vaues in the sequence (3 or more): '))    

    while(pos<3):
        pos = int(input('Out of bounds. Please re-enter (Range 3 or more): '))

    if(choice == 1):
        print(f'Here are the first {pos} values of the Fibonacci sequence: {Fibseq(pos)}')
    elif(choice == 2):
        print(f'Here are the first {pos} values of the Catalan sequence: {Catseq(pos)}')
    elif(choice == 3):
        print(f'Here are the first {pos} values of the Lazy Caterer\'s sequence: {Lazyseq(pos)}')

    loop = input('Would you like to run this program again? (yes or no): ') #lower method provided issues so I just dropped it

print('That\'s all folks, have a great day!')
