"""
- The word Polymorphism is a combination of two Greek words, Poly meaning many
  and Morph meaning forms.

- In programming, polymorphism refers to the same object exhibiting different
  forms and behaviors.

For example, take the Shape Class. The exact shape you choose can be anything.
It can be a rectangle, a circle, a polygon or a diamond. So, these are all
shapes, but their properties are different. This is called Polymorphism.
"""


class Rectangle:
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area2
    def get_area(self):
        # print("1 -------------------------------")
        return (self.width * self.height)


class Circle:
    # initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def get_area(self):
        # print("2 -------------------------------")
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].get_area()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].get_area()))

print("\n +++++++++++++++++++ Using Inheritance ++++++++++++++++++")


class Shape1:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def get_area(self):
        pass


class Rectangle1(Shape1):  # derived form Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def get_area(self):
        return (self.width * self.height)


class Circle1(Shape1):  # derived form Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def get_area(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle1(6, 10), Circle1(7)]
print("Area of rectangle is:", str(shapes[0].get_area()))
print("Area of circle is:", str(shapes[1].get_area()))
