"""
Method Overloading:
------------------
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same
class shares the same method name having different signatures.

Method overloading is used to add more to the behavior of methods and there is no need of more than one
class for method overloading.

Note: Python does not support method overloading. We may overload the methods but can only use the
latest defined method.

In order to include optional arguments, we assign default values to those arguments rather than
creating a duplicate method with the same name. If the user chooses not to assign a value to the
optional parameter, a default value will automatically be assigned to the variable.

If we redefine a method several times and give it different arguments, Python uses the latest method
definition for its implementation.

Advantages of Method Overloading:
---------------------------------
One might wonder that we could simply create new methods to perform different jobs rather than
overloading the same method. However, under the hood, overloading saves us memory in the system.
Creating new methods is costlier compared to overloading a single one.

Since they are memory-efficient, overloaded methods are compiled faster compared to different methods,
especially if the list of methods is long.

An obvious benefit is that the code becomes simple and clean. We don’t have to keep track of
 different methods.

Polymorphism is a very important concept in object-oriented programming. It will come up later on in
the course, but method overloading plays a vital role in its implementation. """


class Employee:
    # defining the properties and assigning them None to the
    def __init__(self, id=None, salary=None, department=None):
        self.ID = id
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def tax(self, title=None):
        return (self.salary * 0.2)

    def salary_per_day(self):
        return (self.salary / 30)


# cerating an object of the Employee class
obj = Employee()

# Printing properties of Steve
print("Demo 1")
obj.demo(1, 2, 3)
print("\n")

print("Demo 2")
obj.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
obj.demo(1, 2, 3, 4, 5)

"""
S.NO	Method Overloading	Method Overriding
1.	In the method overloading, methods or functions must have the same name and
different signatures.Whereas in the method overriding, methods or functions 
must have the same name and same signatures.

2.	Method overloading is a example of compile time polymorphism.	
Whereas method overriding is a example of run time polymorphism.

3.	In the method overloading, inheritance may or may not be required.
Whereas in method overriding, inheritance always required.

4.	Method overloading is performed between methods within the class.
Whereas method overriding is done between parent class and child class methods.

5.	It is used in order to add more to the behavior of methods.	Whereas it is 
used in order to change the behavior of exist methods.

6.	In method overloading, there is no need of more than one class.	Whereas in
method overriding, there is need of at least of two classes. """
