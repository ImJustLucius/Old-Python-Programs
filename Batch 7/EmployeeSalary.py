#Jonathan M Lucius
#The purpose of this program is to calculate employee weekly salary
class Employee:
    def __init__(self, name, ID):
        self._name = name
        self._employeeID = ID
    
    def setName(self, name):
        self._name = name
    
    def setID(self, ID):
        self._employeeID = ID
    
 #   def __str__(self):
  #      return f'Employee: {self.__name}\nID: {self.__employeeID}'

class Engineer:
    def __init__(self, name, ID):
        Employee.__init__(self, name, ID)
        self.__title = ''
        self.__hours = ''
        self.__payrate = ''
    
    def setTitle(self, title):
        self.__title = title
    
    def setHours(self, hours):
        self.__hours = hours
    
    def setPay(self, title):
        PayChart = {
            'Engineering Intern' : 20,
            'Senior Engineer' : 45,
            'Lead Engineer' : 70
        }

        #print(f'\n paychart says {title} = {PayChart[title]}\n')
        self.__payrate = PayChart[title]
    
    def WeekPay(self):
        hours = self.__hours
        prate = float(self.__payrate)

        #print(hours)
        #print(prate)


        if(hours>40):
            overpay = prate*1.5
            overtime = hours-40
            salary = (prate*40) + (overpay*overtime)
        else:
            salary = hours*prate
        
        #print(salary)


        return salary
    
    def __str__(self):
        pay = Engineer.WeekPay(self)
        return f'Employee: {self._name}\nID: {self._employeeID}\nThis employee\'s Pay for this week is: ${pay:.2f}'

def main():
    name = input("Please enter the Employee's name: ")
    id = input("Please enter the Employee's ID: ")
    title = input("Please enter the Employee's title: ")
    hours = int(input("Please enter the amount of hours worked (Must be between 0 and 60 inclusive): "))
    if(hours>60):
        while(hours<0 or hours>60):
            hours = int(input("Invalid, try again (input must be between 0 and 60 inclusive): "))

    tester = Engineer(name, id)
    tester.setTitle(title)
    tester.setHours(hours)
    tester.setPay(title)

    print(tester)
    #print('testing')

main()