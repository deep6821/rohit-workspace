"""
“Separate the construction of a complex object from its representation so that the same construction process can create
different representations.”

It allows you to construct complex objects step by step. Here using the same construction code, we can produce different
types and representations of the object easily.

It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented
programming.

Problem without using the Builder Method:
-----------------------------------------

Imagine you want to join one of the elite batches of GeeksforGeeks. So, you will go there and ask about the Fee
structure, timings available, and batches about the course you want to join. After looking at the system, they will tell
you about the courses, their Fee structures, timings available and batches. That's it.

Our main purpose is to design the system flexible, reliable, organized and lubricative. what Unexperienced developers
will do is that they will create a separate and unique class for each and every course provided by GeeksforGeeks. Then
they will create separate object instantiation for each and every class although which is not required every time.
The main problem will arise when GeeksforGeeks will start new courses and developers have to add new classes as well
because their code is not much flexible.
"""

if 0:
    # Without using the Builder method
    class DSA(object):
        """Class for Data Structures and Algorithms"""

        def Fee(self):
            self.fee = 8000

        def available_batches(self):
            self.batches = 5

        def __str__(self):
            return "DSA"


    class SDE(object):
        """Class for Software development Engineer"""

        def Fee(self):
            self.fee = 10000

        def available_batches(self):
            self.batches = 4

        def __str__(self):
            return "SDE"


    class STL(object):
        """class for Standard Template Library of C++"""

        def Fee(self):
            self.fee = 5000

        def available_batches(self):
            self.batches = 7

        def __str__(self):
            return "STL"


    # main method
    if __name__ == "__main__":
        sde = SDE()  # object for SDE
        dsa = DSA()  # object for DSA
        stl = STL()  # object for STL

        print(f'Name of Course: {sde} and its Fee: {sde.fee}')
        print(f'Name of Course: {stl} and its Fee: {stl.fee}')
        print(f'Name of Course: {dsa} and its Fee: {dsa.fee}')

if 1:
    class Course:
        def __init__(self):
            self.Fee()
            self.available_batches()

        def Fee(self):
            raise NotImplementedError

        def available_batches(self):
            raise NotImplementedError

        def __repr__(self):
            return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)


    class DSA(Course):
        """Class for Data Structures and Algorithms"""

        def Fee(self):
            self.fee = 8000

        def available_batches(self):
            self.batches = 5

        def __str__(self):
            return "DSA"


    class SDE(Course):
        """Class for Software Development Engineer"""

        def Fee(self):
            self.fee = 10000

        def available_batches(self):
            self.batches = 4

        def __str__(self):
            return "SDE"


    # concrete course
    class STL(Course):
        """Class for Standard Template Library"""

        def Fee(self):
            self.fee = 5000

        def available_batches(self):
            self.batches = 7

        def __str__(self):
            return "STL"


    # Complex Course
    class ComplexCourse:

        def __repr__(self):
            return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)


    class Complexcourse(ComplexCourse):

        def Fee(self):
            self.fee = 7000

        def available_batches(self):
            self.batches = 6


    # construct course
    def construct_course(cls):
        course = cls()
        course.Fee()
        course.available_batches()

        return course  # return the course object


    # main method
    if __name__ == "__main__":
        dsa = DSA()  # object for DSA course
        sde = SDE()  # object for SDE course
        stl = STL()  # object for STL course

        complex_course = construct_course(Complexcourse)
        print(complex_course)
