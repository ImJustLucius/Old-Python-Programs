#Jonathan M Lucius
#The purpose of this program is to relay the number of given values that are less than the given limit.

def  limit_check(container, max):
    print('The numbers: ',end='')

    for x in container:
        if(x<max):
            print(x,end=', ')
    
    print(f'are less than the limit: {max}')

def main():
    global tank
    global limit
    tank = []
    tank_size = int(input('How many numbers do you have? '))
    
    for x in range(tank_size):
        tank.append(int(input('Please input a number: ')))
    
    limit = int(input('Please input the limit: '))

main()

limit_check(tank,limit) 