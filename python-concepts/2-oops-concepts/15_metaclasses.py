""""
metaclass: A metaclass is the class of a class; it defines how a class behaves.
----------

Classes are used to make objects. However, a class itself is an object and, just like any other
object, it’s an instance of something: a ​metaclass.

Hence, if we want to modify the behavior of classes, we will need to write our own custom metaclass.

The default metaclass is type. This means that just like an object is of the type class, a class
itself is of the type, type.

********************************************************************************
Class object --> is an instance of ==> Class --> is an instance of ==> Metaclass
********************************************************************************
"""


class Test:
    pass


test = Test()
print(type(test))  # <class '__main__.Test'>
print(type(Test))  # <class 'type'>

"""
Defining custom metaclasses:
---------------------------
The type() function can be used to directly define classes by passing it through:

the class name.
the tuple of the base classes inherited by the class.
a dictionary containing the class’ methods and variables.

new_class = type('newClass', (), {foo(), dob:1997})
new_class --> class variable
newClass --> class name
() --> base classes inherited by the class
foo() --> methods of our class and dob:1997 --> variables of our class

"""

"""
To create a custom metaclass, we first have to inherit the default metaclass, "type", and then
override its __new__() and __init__() methods.  

The following code defines a metaclass with a custom __new__() method which defines a new 
attribute "x" in the class. The Foo class inherits the attributes of its metaclass Meta
"""


class Meta(type):
    # overriding the new method of the metaclass
    def __new__(cls, name, bases, dct):
        print("----->", name, ":", bases, "::", dct)
        x = super().__new__(cls, name, bases, dct)
        # defining that each class with this metaclass
        # should have a variable, x with a default value
        x.attr = 100
        return x


# defining a class with Meta as its metaclass instead of type
class Foo(metaclass=Meta):
    pass


# printing the variables in our newly defined class
print(Foo.attr)

"""
Uses of custom metaclasses:
--------------------------
Metaclasses can be applied in logging, registration of classes at creation time, profiling, and 
others. They propagate down the inheritance hierarchies, allowing all subclasses to inherit their 
attributes and methods. This property is particularly useful if we want our classes to have specific 
attributes, automatically, at the time of their creation.
"""

def extendList(val, lst=[]):
    lst.append(val)
    return lst

lst1 = extendList(1)
lst2 = extendList(11,[])
lst3 = extendList('x')
print(lst1)
print(lst2)
print(lst3)