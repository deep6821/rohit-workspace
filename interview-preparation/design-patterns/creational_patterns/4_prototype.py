"""
- It aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of
  the concrete implementation of their classes.
- Generally, here the object is created by copying a prototypical instance during run-time.
- It is highly recommended to use Prototype Method when the object creation is an expensive task in terms of time and
  usage of resources and already there exists a similar object.
- This method provides a way to copy the original object and then modify it according to our needs.

Advantages:
-----------
1. Less number of SubClasses : All the other Creational Design Patterns provides a lot of new subClasses which are
   definitely not easy to handle when we are working on a large project. But using Prototype Design Patterm, we get
   rid of this.
2. Provides varying values to new objects: All the highly dynamic systems allows you define new behavior through object
   composition by specifying values for an object’s variables and not by defining new classes.
3. Provides varying structure to new objects: General all the applications build objects from parts and subparts. For
   convenience, such applications often allows you instantiate complex, user-defined structures to use a specific
   subcircuit again and again

Disadvantages:
--------------
1. Abstraction: It helps in achieving the abstraction by hiding the concrete implementation details of the class.
2. Waste of resources at lower level: It might be proved as the overkill of resources for a project that uses very few
   objects

Applicability:
--------------
1. Independency from Concrete Class: Prototype method provides the way to implement the new objects without depending
   upon the concrete implementation of the class.
2. Recurring problems : Prototype method is also used to solve the recurring and complex problems of the software
   development.

"""

if 1:
    """
    Suppose we have a Shape class that produces different shapes such as circle, rectangle, square, etc and we already 
    have an object of it. Now we want to create the exact copy of this object. How an ordinary developer will go?
    He/She will create a new object of the same class and will apply all the functionalities of the original objects and
    copy their values. But we can not copy each and every field of the original object as some may be private and 
    protected and are not available from the outside of the object itself. Problems are not over here! you also become 
    dependent on the code of other class which is certainly not a good practice in Software Development
    """


    class DSA():
        """Class for Data Structures and Algorithms"""

        def Type(self):
            return "Data Structures and Algorithms"

        def __str__(self):
            return "DSA"


    class SDE():
        """Class for Software development Engineer"""

        def Type(self):
            return "Software Development Engineer"

        def __str__(self):
            return "SDE"


    class STL():
        """class for Standard Template Library of C++"""

        def Type(self):
            return "Standard Template Library"

        def __str__(self):
            return "STL"


    # main method
    if __name__ == "__main__":
        sde = SDE()  # object for SDE
        dsa = DSA()  # object for DSA
        stl = STL()  # object for STL
        print(f'Name of Course: {sde} and its type: {sde.Type()}')
        print(f'Name of Course: {stl} and its type: {stl.Type()}')
        print(f'Name of Course: {dsa} and its type: {dsa.Type()}')

if 1:
    """
    """

    from abc import ABCMeta, abstractmethod
    import copy


    class CoursesAtGFG(metaclass=ABCMeta):
        def __init__(self):
            self.id = None
            self.type = None

        @abstractmethod
        def course(self):
            pass

        def get_type(self):
            return self.type

        def get_id(self):
            return self.id

        def set_id(self, sid):
            self.id = sid

        def clone(self):
            return copy.copy(self)


    class DSA(CoursesAtGFG):
        def __init__(self):
            super().__init__()
            self.type = "Data Structures and Algorithms"

        def course(self):
            print("Inside DSA::course() method")


    class SDE(CoursesAtGFG):
        def __init__(self):
            super().__init__()
            self.type = "Software Development Engineer"

        def course(self):
            print("Inside SDE::course() method.")


    class STL(CoursesAtGFG):
        def __init__(self):
            super().__init__()
            self.type = "Standard Template Library"

        def course(self):
            print("Inside STL::course() method.")


    class CoursesAtGFGCache:
        # cache to store useful information
        cache = {}

        @staticmethod
        def get_course(sid):
            COURSE = CoursesAtGFGCache.cache.get(sid, None)
            return COURSE.clone()

        @staticmethod
        def load():
            sde = SDE()
            sde.set_id("1")
            CoursesAtGFGCache.cache[sde.get_id()] = sde

            dsa = DSA()
            dsa.set_id("2")
            CoursesAtGFGCache.cache[dsa.get_id()] = dsa

            stl = STL()
            stl.set_id("3")
            CoursesAtGFGCache.cache[stl.get_id()] = stl


    # main function
    if __name__ == '__main__':
        CoursesAtGFGCache.load()

        sde = CoursesAtGFGCache.get_course("1")
        print(sde.get_type())

        dsa = CoursesAtGFGCache.get_course("2")
        print(dsa.get_type())

        stl = CoursesAtGFGCache.get_course("3")
        print(stl.get_type())
