# Python Class Variables


class Employee:
    # ? These are the class variables
    num_of_employees = 0
    raise_amount = 1.04

    # ? This is the class initializing method aka constructor

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # ? Increment the number of employees by 1 whenever a new employee object is created
        Employee.num_of_employees += 1

    def fullname(self):
        # ? Old method for a formatted string
        # return '{} {}'.format(self.first, self.last)

        # ? New method for a formatted string
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# ? Creating two instances of the Class Employee
emp_1 = Employee('Michael', 'Le', 100000)
emp_2 = Employee('Phuc', 'Le', 200000)

print(emp_1.fullname(), emp_1.pay, emp_1.email)
print(f'{emp_2.fullname()} makes {emp_2.pay}K and contact is {emp_2.email}')

# ? Using the class variables
print('Number of Employees: {}'.format(Employee.num_of_employees))

# ? calling the apply_raise method on these employee objects
emp_1.apply_raise()
emp_2.apply_raise()

# ? pay has been increaed by 4%
print(emp_1.pay)
print(emp_2.pay)

# ? raising an employee instance pay that doesn't impact the other instances
emp_1.raise_amount = 1.10
emp_1.apply_raise()
print(emp_1.pay)

# ? emp_2 pay stays the same
print(emp_2.pay)
