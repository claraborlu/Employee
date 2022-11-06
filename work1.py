import work 

def main():
    # A while loop condition is created in case there is more than one employee

    again = 'y'

    while again == 'y':
        name = input("Enter the name of the employee: ")
        emp_num = int(input("Enter the number of the employee: "))
        shift_num = int(input("Enter either 1 or 2 to know the shift time for the employee: "))
        rate = float(input("Enter the hourly rate that is earned by the employee: "))

        print()

        worker = work.ProductionWorker(name, emp_num, shift_num, rate)
        print(f'the name of the employee is {worker.get_name()}')
        print(f'the employee will work during the {worker.get_shift_number(shift_num)}')
        print(f'the rate of the employee is {worker.get_pay_rate()}')
        print()

        again = input("if you want to enter another data, the type y: ")

main()


