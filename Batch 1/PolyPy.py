#Jonathan M Lucius
#This program will draw a polygon using inputted length and # of sides
import turtle

sides = int(input('Input the number of sides (range of 3-12): '))
while(sides<3 or sides>12):
    sides = int(input('Outside of the range, reinput: '))

length = int(input('Input the length of the sides (must be greater than 50): '))
while(length<=50):
    length = int(input('Outside of the range, reinput: '))

angle = (180*(sides-2))/sides
turn = 180-angle

for x in range(sides):
    turtle.forward(length)
    turtle.right(turn)

if(sides==3): 
    turtle.write('Triangle')
elif(sides==4):
        turtle.write('quadrilateral')
elif(sides==5):
        turtle.write('pentagon')
elif(sides==6):
        turtle.write('hexagon')
elif(sides==7):
        turtle.write('heptagon')
elif(sides==8):
        turtle.write('octagon')
elif(sides==9):
        turtle.write('nonagon')
elif(sides==10):
        turtle.write('decagon')
elif(sides==11):
        turtle.write('hendecagon')
elif(sides==12):
        turtle.write('dodecagon')

input('Press ENTER to exit...')