#Jonathan M Lucius
#This script will predict the approximate size of a population of organisms

pop = 0
inc = 0
days = 0

while pop<1:
    pop = float(input('input the statring number of organisms: '))

while inc<1:
    inc = float(input('Input the daily increase (percentage): '))

inc /= 100

while days<1:
    days = int(input('Input the number of days: '))

print('Day          Population\n-----------------------')

for x in range(1,days+1):
    print(f'{x}             {pop:.6f}')
    pop += pop * inc
