"""
Method Overriding:
-----------------
- Method overriding is an example of run time polymorphism. It is the process
  of redefining a parent class’s method in a subclass.

- In other words, if a subclass provides a specific implementation of a method
  that had already been defined in one of its parent classes, it is known as
  method overriding.

- It is used to change the behavior of existing methods and there is a need for
  at least two classes for method overriding. In method overriding, inheritance
  always required as it is done between parent class(superclass) and child
  class(child class) methods.


Advantages and Key Features of Method Overriding:
-------------------------------------------------
- The derived classes can give their own specific implementations to inherited
  methods without modifying the parent class methods.

- For any method, a child class can use the implementation in the parent class
  or make its own implementation.

- Method Overriding needs inheritance and there should be at least one derived
  class to implement it.

- The method in the derived classes usually have a different implementation
  from one another.
"""


class Shape:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def get_area(self):
        pass


class Rectangle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def get_area(self):
        return self.width * self.height


class Circle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def get_area(self):
        return self.radius * self.radius * 3.142


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].get_area()))
print("Area of circle is:", str(shapes[1].get_area()))
