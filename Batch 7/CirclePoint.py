#Jonathan M Lucius
# The purpose of this code is to determine if a given point is on the inside, outside, or rim of a circle.
import math

center_x = float(input("Please input the x coordinate of the circle's center: "))
center_y = float(input("Please input the y coordinate of the circle's center: "))
radius = float(input('Please input the radius of the circle: '))

if(radius<=0):
    while(radius<=0):
        radius = float(input('Radius must be greater than 0, please reinput: '))

point_x = float(input('PLease input the x coordinate of the point: '))
point_y = float(input('PLease input the y coordinate of the point: '))
distance = (((point_x-center_x)**2) + ((point_y-center_y)**2))**(1/2)

print(f'The distance between the center({center_x},{center_y}) and the point ({point_x},{point_y}) is {distance:.2f}')

if(distance>radius):
    print(f'the point ({point_x},{point_y}) is outside the circle.')
elif(distance==radius):
    print(f'The point ({point_x},{point_y}) is on the circle.')
elif(distance<radius):
    print(f'The point ({point_x},{point_y}) is inside the circle.')
else:
    print('Something went wrong, please try the program again...')