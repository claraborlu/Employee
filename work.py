# This program creates a class for employee and production worker as a sub class

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

# A sub class is created from the Employee class that was created earlier
class ProductionWorker(Employee):
    def __init__(self, name, number,shift_number, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    
# A condition to return either day or night when the user enters the number of the shift
    def get_shift_number(self,shift_num):
        if shift_num == 1:
            return "Day"
        else:
            return "Night"

# A method that returns the pay_rate of the employee
        

    def get_pay_rate(self):
        return self.__pay_rate
   
