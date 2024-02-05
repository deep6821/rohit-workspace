"""
What are Abstract Base Classes?
-------------------------------
- Duck typing is useful as it simplifies the code and the user can implement the 
  functions without worrying about the data type. But this may not be the case 
  all the time. The user might not follow the instructions to implement the 
  necessary steps for duck typing. To cater to this issue, Python introduced 
  the concept of Abstract Base Classes, or ABC.
  
Abstract Base Classes: define a set of methods and properties that a class must 
                       implement in order to be considered a duck-type instance 
                       of that class. """

"""
Why use Abstract Base Classes:
------------------------------
In the example below, you can see that an instance of Shape can be created even 
though an object from this class cannot stand on its own. 

Square class, which is the child class of Shape, actually implements the 
methods, area() and perimeter(), of the Shape class. Shape class should provide 
a blueprint for its child classes to implement methods in it. 

To prevent the user from making a Shape class object, we use abstract base 
classes.
"""


class Shape:  # Shape is a child class of ABC
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
square = Square(4)

print("\n -------------------------------------------------------------------")
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with
#                  # abstract methods area, perimeter
# square = Square(4)  # TypeError: Can't instantiate abstract class Shape with
#                     # abstract methods area, perimeter


print("\n -------------------------------------------------------------------")


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square = Square(5)
print(square.area())
shape = Shape()  # TypeError: Can't instantiate abstract class Shape with
# abstract methods area, perimeter


"""
An abstract class has some features, as follows:
------------------------------------------------
1. An abstract class doesn’t contain all of the method implementations required to work completely,
which means it contains one or more abstract methods.
An abstract method is a method that just has a declaration but does not have a detail implementation.

2. An abstract class cannot be instantiated. It just provides an interface for subclasses to avoid
code duplication. It makes no sense to instantiate an abstract class.

3. A derived subclass must implement the abstract methods to create a concrete class that fits the
interface defined by the abstract class. Therefore it cannot be instantiated unless all of its
bstract methods are overridden.

Define Abstract Class in Python
-------------------------------
Python comes with a module called abc which provides useful stuff for abstract class.

We can define a class as an abstract class by abc.ABC and define a method as an abstract method by
abc.abstractmethod. ABC is the abbreviation of abstract base class.

Note: A class is not real abstract if it has abstract methods but not inherit from abc.ABC, which
means it can be instantiated. For example:
"""
