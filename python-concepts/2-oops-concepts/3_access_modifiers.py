"""
- In Python, we can impose access restrictions on different data members and member functions.
- The restrictions are specified through access modifiers.
- Access modifiers are tags we can associate with each member to define which parts of the
  program can access it directly.
- There are two types of access modifiers in Python. Let’s take a look at them one by one. """

"""
1. Public attributes: are those that be can be accessed inside the class and outside the class.
   - Technically in Python, all methods and properties in a class are publicly available by default.
     If we want to suggest that a method should not be used publicly, we have to declare it as private
    explicitly. """


class Employee:
    def __init__(self, id, salary):
        # all properties are public
        self.id = id
        self.salary = salary

    def display_id(self):
        print("ID:", self.id)


obj = Employee(3789, 2500)
obj.display_id()
print(obj.salary)


print("\n ------------------------------------------------------------------")
"""
2. Private attributes: cannot be accessed directly from outside the class but can be accessed from 
inside the class.

The aim is to keep it hidden from the users and other classes. Unlike in many different languages, 
it is not a widespread practice in Python to keep the data members private since we do not want to 
create hindrances for the users. We can make members private using the double underscore __ prefix """


class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.__salary = salary  # salary is a private property

    def display_salary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __display_id(self):  # displayID is a private method
        print("ID:", self.id)


obj = Employee(3789, 2500)
print("ID:", obj.id)
obj.display_salary()
# print("Salary:", obj.__salary)  # Error: AttributeError: 'Employee' object has no attribute '__salary'
# obj.__display_id()  # Error: AttributeError: 'Employee' object has no attribute '__display_id'


print("\n ------------------------------------------------------------------")
""" Accessing Private Attributes in the Main Code """


class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.__salary = salary  # salary is a private property


obj = Employee(3789, 2500)
print(obj._Employee__salary)  # accessing a private property
