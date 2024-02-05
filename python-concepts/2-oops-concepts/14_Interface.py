""""
Introduction to Interface in Python
-----------------------------------
- An interface is used to specify behavior that classes must implement.
- Abstract classes are used to implement interfaces and are classes that contain one or more abstract methods.
- An abstract method is a method that is declared, but contains no implementation.

Ex:
One of our repos contains a class that pulls a bunch of data over the network, and generally takes a pretty long
time to run. As it turned out, we didn’t want to spend all this time gathering data every time we ran the service,
so we decided to create a dummy class that we could swap in for the real one. In order for everything to continue
working, both classes needed to expose identical looking functions.

Instead of relying on Python’s duck typing, this sounded like a great place to define an interface that both
classes could inherit from, to ensure the callers that nothing would break regardless of which class was being
used.

How to Create Interface in Python?
----------------------------------
1. Informal Interfaces
2. Formal Interfaces

Informal Interfaces:
+++++++++++++++++++
Python informal interface is also a class which defines methods that can be overridden, but without force
enforcement. An informal interface also called Protocols or Duck Typing.

**** The duck typing is actually we execute a method on the object as we expected an object to have, instead of
checking the type of an object. If it’s beaver is same as we expected, then we will be fine and go farther,
else if it does not, things might get wrong and for safety, we use a try..except block or hasattr to handle
the exceptions to check the object have the particular method or not. ****

Ex: __len__, __iter__, __contains__ and all, which are used to perform some operation or set of protocols.

class Fruits :
    def __init__( self, ele):
        self.__ele = ele

    def __contains__( self, ele):
        return ele in self.__ele

    def __len__( self ):
        return len( self.__ele)

Fruits_list = Fruits([ "Apple", "Banana", "Orange" ])
print(len(Fruits_list))
print("Apple" in Fruits_list)
print("Mango" in Fruits_list)
print("Orange" not in Fruits_list)

Formal Interfaces:
++++++++++++++++++
import abc
class Myinterface(abc.ABC) :
    @abc.abstractclassmethod
    def disp():
        pass

class Myclass(Myinterface) :
    pass

o1 = Myclass( ) # TypeError: Can't instantiate abstract class Myclass with abstract methods disp

In the above code, the Myclass class inheriting abstract class Myinterface, but not provided the
implementation for the disp() abstract method and so the class Myclass also becomes as abstract
class and hence cannot be instantiated.

-----------------------------------------------------------------------------
"""
# Examples of Interface in Python
import abc


# Example #1
class Myinterface(abc.ABC):
    @abc.abstractmethod
    def disp(self):
        pass


class Myclass(Myinterface):
    def disp(self):
        pass


o1 = Myclass()
print("\n 1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Example #2
class Myinterface(abc.ABC):
    @abc.abstractmethod
    def disp(self):
        pass


class Myclass(Myinterface):
    def disp(self):
        print(" Hello from Myclass ")


o1 = Myclass()
o1.disp()
print("\n 2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Example #3
class FourWheelVehicle(abc.ABC):
    @abc.abstractmethod
    def SpeedUp(self):
        pass


class Car(FourWheelVehicle):
    def SpeedUp(self):
        print(" Running! ")


s = Car()
print(isinstance(s, FourWheelVehicle))  # True
print("\n 3+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Example #4
class FourWheelVehicle(abc.ABC):
    @abc.abstractmethod
    def SpeedUp(self):
        pass


class Car(FourWheelVehicle):
    def SpeedUp(self):
        print(" Running! ")


class TwoWheelVehicle(abc.ABC):
    @abc.abstractmethod
    def SpeedUp(self):
        pass


class Bike(TwoWheelVehicle):
    def SpeedUp(self):
        print(" Running!.. ")


a = Bike()
s = Car()
print(isinstance(s, FourWheelVehicle))  # True
print(isinstance(s, TwoWheelVehicle))  # False
print(isinstance(a, FourWheelVehicle))  # False
print(isinstance(a, TwoWheelVehicle))  # True
