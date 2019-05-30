# Python Classes and Instances


class Employee:
    # ? this is the class initializing method aka constructor

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        # ? Old method for a formatted string
        # return '{} {}'.format(self.first, self.last)

        # ? New method for a formatted string
        return f'{self.first} {self.last}'


emp_1 = Employee('Michael', 'Le', 100000)
emp_2 = Employee('Phuc', 'Le', 200000)

print(emp_1.fullname(), emp_1.pay, emp_1.email)
print(f'{emp_2.fullname()} makes {emp_2.pay}K and contact is {emp_2.email}')
