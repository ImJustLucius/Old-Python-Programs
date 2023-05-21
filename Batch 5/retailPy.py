#Jonathan M Lucius
#The purpose of this program is to create a chart of user-prompted retail Items

class Retail_Item:
    def __init__(self, type, count, price):
        self.__type = type
        self.__count = count
        self.__price = price
    
    def __str__(self):
        return f'{self.__type:17s}{self.__count:<10}${self.__price:<8.2f}'
        
def main():
    name1 = input('Enter the 1st item name: ')
    count1 = input('Enter the 1st item amount: ')
    price1 = float(input('Enter the 1st item price: '))

    Item1 = Retail_Item(name1, count1, price1)

    name2 = input('Enter the 2nd item name: ')
    count2 = input('Enter the 2nd item amount: ')
    price2 = float(input('Enter the 2nd item price: '))

    Item2 = Retail_Item(name2, count2, price2)

    print('Here are is your shopping cart:\n''Item'+(' '*13)+'Count'+(' '*5)+'Price\n'+'-'*35)
    print(Item1)
    print(Item2)

main()
