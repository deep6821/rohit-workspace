"""
Instance Methods:
-----------------
They are most widely used methods. Instance method receives the instance of the class as the first 
argument, which by convention is called self, and points to the instance of our class 'Employee'.

However it can take any number of arguments. Using the self parameter, we can access the other attributes 
and methods on the same object and can change the object state. 

Also, using the self.__class__ attribute, we can access the class attributes, and can change the 
class state as well. Therefore, instance methods gives us control of changing the object as well as
the class state. """


class Employee:
    # defining the initializer
    def __init__(self, id=None, salary=None, department=None):
        self.id = id
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salary_per_day(self):
        return (self.salary / 30)


if __name__ == "__main__":
    # initializing an object of the Employee class
    obj = Employee(3789, 2500, "Human Resources")
    # Printing properties of Steve
    print("ID =", obj.id)
    print("Salary", obj.salary)
    print("Department:", obj.department)
    print("Tax paid by Steve:", obj.tax())
    print("Salary per day of Steve", obj.salary_per_day())


print("\n--------------------------------------------------------------------")
"""
Class Methods:
-------------
A class method accepts the class as an argument to it which by convention is called 'cls'. It take 
the cls parameter, which points to the class 'Test' instead of the object of it. It is declared with 
the @classmethod decorator.

Class methods are bound to the class and not to the object of the class. They can alter the class 
state that would apply across all instances of class but not the object state. 

Class methods are accessed using the class name and can be accessed without creating a class object. """


class Player:
    team_name = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def get_team_name(cls):
        return cls.team_name


print(Player.get_team_name())


print("\n--------------------------------------------------------------------")
"""
Static Methods:
---------------
A static method is marked with a @staticmethod decorator to flag it as static. It does not receive 
an implicit first argument (neither self nor cls).

It can also be put as a method that “does’t know its class”. Hence a static method is merely 
attached for convenience to the class object. Hence static methods can neither modify the object 
state nor class state. They are primarily a way to namespace our methods.

They are used as utility functions inside the class or when we do not want the inherited classes

Static methods can be accessed using the class name or the object name. """


class Player1:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player1('lol')
p1.demo()  # accessing call method using object of the class
Player1.demo()  # accessing the class method using class name
