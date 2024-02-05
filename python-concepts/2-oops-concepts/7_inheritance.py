"""
- Inheritance provides a way to create a new class from an existing class.
- The new class is a specialized version of the existing class such that it
  inherits all the non-private fields (variables) and methods of the existing
  class. The existing class is used as a starting point or as a base to create
  the new class.

The IS A Relationship:
----------------------
Square IS A shape
Python IS A programming language
Car IS A vehicle

So, from the above descriptions regarding inheritance, we can conclude that we
can build new classes by extending existing classes.

Existing Class                      Derived Class
Shape                               Square
Programming Language                Python
Vehicle                             Car

** we cannot use inheritance whenever an IS A relationship doesn’t exist
between the classes.

Types of Inheritance:
--------------------
Based upon parent classes and child classes, there are the following five types of inheritance:

1. Single
2. Multi-level
3. Hierarchical
4. Multiple
5. Hybrid """

print("\n--------------------- Single Inheritance --------------------------")
"""
Single Inheritance: there is only a single class extending from another class.
                    We can take the example of the Vehicle class, as the parent
                    class, and the Car class, as the child class. """


class Vehicle:  # parent class
    def set_top_Speed(self, speed):  # defining the set
        self.top_speed = speed
        print("Top speed is set to", self.top_speed)


class Car(Vehicle):  # child class
    def open_trunk(self):
        print("Trunk is now open.")


corolla = Car()  # creating an object of the Car class
corolla.set_top_Speed(220)  # accessing methods from the parent class
corolla.open_trunk()  # accessing method from its own class

print("\n---------------------- Multi-level Inheritance ---------------------")
"""
Multi-level Inheritance: When a class is derived from a class which itself is 
                         derived from another class, it’s called Multilevel 
                         Inheritance. We can extend the classes to as many 
                         levels as we want to. """


class Vehicle:  # parent class
    def set_top_speed(self, speed):  # defining the set
        self.top_speed = speed
        print("Top speed is set to", self.top_speed)


class Car(Vehicle):  # child class of Vehicle
    def open_trunk(self):
        print("Trunk is now open.")


class Hybrid(Car):  # child class of Car
    def turn_on_hybrid(self):
        print("Hybrid mode is now switched on.")


prius_prime = Hybrid()  # creating an object of the Hybrid class
prius_prime.set_top_speed(220)  # accessing methods from the parent class
prius_prime.open_trunk()  # accessing method from the parent class
prius_prime.turn_on_hybrid()  # accessing method from the parent class

print("\n-------------------- Hierarchical Inheritance  ---------------------")
"""
Hierarchical Inheritance: When more than one class inherits from the same class
                          it’s referred to as hierarchical inheritance. In 
                          hierarchical inheritance, more than one class extends 
                          as per the requirement of the design, from the same 
                          base class. The common attributes of these child 
                          classes are implemented inside the base class.
"""


class Vehicle:  # parent class
    def set_top_speed(self, speed):  # defining the set
        self.top_speed = speed
        print("Top speed is set to", self.top_speed)


class Car(Vehicle):  # child class of Vehicle
    pass


class Truck(Vehicle):  # child class of Car
    pass


corolla = Car()  # creating an object of the Car class
corolla.set_top_speed(220)  # accessing methods from the parent class

volvo = Truck()  # creating an object of the Truck class
volvo.set_top_speed(180)  # accessing methods from the parent class

print("\n-------------------- Multiple Inheritance  ---------------------")
"""
Multiple Inheritance: When a class is derived from more than one base class, 
                      i.e., when a class has more than one immediate parent 
                      class, it is called Multiple Inheritance. """


class CombustionEngine():
    def set_tank_capacity(self, tank_capacity):
        self.tank_capacity = tank_capacity


class ElectricEngine():
    def set_charge_capacity(self, charge_capacity):
        self.charge_capacity = charge_capacity


# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def print_details(self):
        print("Tank Capacity:", self.tank_capacity)
        print("Charge Capacity:", self.charge_capacity)


car = HybridEngine()
car.set_charge_capacity("250 W")
car.set_tank_capacity("20 Litres")
car.print_details()

print("\n-------------------- Hybrid Inheritance  ---------------------")
"""
Hybrid Inheritance: A type of inheritance which is a combination of Multiple 
                    and Multi-level inheritance is called hybrid inheritance.
"""


class Engine:  # Parent class
    def set_power(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def set_tank_capacity(self, tank_capacity):
        self.tank_capacity = tank_capacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def set_charge_capacity(self, charge_capacity):
        self.charge_capacity = charge_capacity


# Child class inherited from CombustionEngine and ElectricEngine


class HybridEngine(CombustionEngine, ElectricEngine):
    def print_details(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tank_capacity)
        print("Charge Capacity:", self.charge_capacity)


car = HybridEngine()
car.set_power("2000 CC")
car.set_charge_capacity("250 W")
car.set_tank_capacity("20 Litres")
car.print_details()
