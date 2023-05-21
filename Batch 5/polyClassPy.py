#Jonathan M Lucius
#The purpose of this program is to use classes and functions to describe polygons
import math

class Polygon:

    __numSides = 0
    __sidelen = 0.0

    def __init__(self):
        self.__numSides = 0
        self.__sidelen = 0.0
    
    def getSideNum(self):
        return print(f'Number of Sides: {self.__numSides}')
    
    def getSideLen(self):
        return print(f'Side Length: {self.__sidelen}')
    
    def newSideNum(self, num):
        self.__numSides = num
    
    def newSideLen(self, length):
        self.__sidelen = length
    
    def Perimeter(self):
        perim = self.__numSides * self.__sidelen
        return print(f'Perimter: {perim:.3f}')
    
    def Area(self):
        num = self.__numSides
        length = self.__sidelen
        area = (num*(length**2))/(4*(math.tan(math.pi/num)))
        return print(f'Area: {area:.3f}')
    
def main():
    Triangle = Polygon()
    
    numSides = int(input('Please enter the number of sides on your polygon (3 sides or more): '))
    
    while(numSides<3):
        numSides = int(input('Invalid input, please re-enter: '))
    
    sideLen = float(input('Please enter the length of each side: '))
    
    while(sideLen<0.1):
        sideLen = float(input('Invalid input, please re-enter: '))
    
    print('Here are the attributes of your Polygon: ')

    Triangle.newSideNum(numSides)
    
    Triangle.newSideLen(sideLen)
    
    Triangle.getSideLen()
    Triangle.getSideNum()
    Triangle.Perimeter()
    Triangle.Area()

    
    '''
    print(f'Polygon Attributes\nNumber of Sides: {Triangle.getSideNum()}\nSide length: {Triangle.getSideLen()}\
       \nPerimeter: {Triangle.Perimeter()}\nArea: {Triangle.Area():.3f}')
    '''

main()
    