"""
Class:
------
- Class is basically a blueprint for creating instances.
- Class is allow us to logically group our data and function.
- Data and function that are associated with a specific class, we called them attributes and methods.

- A variable that is associated with a class ---> attributes
- A function that is associated with a class ---> method.

Object:
-------
- An object is an instance of a class.
- An instance is a copy of the class with actual.


class Employee:                 class Employee:
    pass                            def __init__(self, f, l):
                                        self.first = f
                                        self.last = l

e1 = Employee()
e2 = Employee()
e1.first = "Rohit"
e1.last = "Pandey"
e2.first = "Test"
e2.last = "User"


Instance variables and class variables:
---------------------------------------
class Employee:
    num_of_emps = 0  # class variable
    raise_amount = 1.04  # class variable
    def __init__(self, first, last, pay):
        self.first = first  # instance variable
        self.last = last    # instance variable
        self.pay = pay      # instance variable
        Employee.num_of_emps +=1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

e1 = Employee('Rohit', 'Pandey', 50)
e2 = Employee('Test', 'User', 60)

class variable                                  instance variable
- class variables are variables whose value     Whose value is assigned inside a constructor or
is assigned a class.                            method itself.

- class attributes belong to class itself,      Instance attributes are not shared by objects. Every
they will be shared by all the instances.       objects has it's own copy of the instance attributes
                                                (In the case of class attributes all object referers
                                                to a single copy)

"""

