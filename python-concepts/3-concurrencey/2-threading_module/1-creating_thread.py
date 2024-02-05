"""
Creating Threads:
-----------------
We can create threads in Python using the Thread class.

Thread constructor:
-------------------
Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)
   1. group argument: is reserved for future extensions.
   2. target argument: is the code that the thread being created will execute.
      It can be any callable object. A callable object can be a function or an
      object of a class that has the __call__ method
   3. name argument: name of the thread
   4. args and kwargs argument: we can pass the arguments to the target either
      as a tuple args or as a dictionary of key value pairs using kwargs.
   5. daemon argument: boolean specifying if the thread being created should
      be treated as a daemon thread.
"""
from threading import Thread
from threading import current_thread


def thread_task(a, b, c, key1, key2):
    print("{0} received the arguments: {1} {2} {3} {4} {5}".format(
        current_thread().getName(), a, b, c, key1, key2))


myThread = Thread(group=None,  # reserved
                  target=thread_task,  # callable object
                  name="demoThread",  # name of thread
                  args=(1, 2, 3),  # arguments passed to the target
                  kwargs={
                      'key1': 777,
                      'key2': 111
                  },  # dictionary of keyword arguments
                  daemon=None  # set true to make the thread a daemon
                  )

myThread.start()  # start the thread
myThread.join()  # wait for the thread to complete

"""
Main Thread:
------------
The astute reader would realize that there has to be another thread that is 
actually executing the code we wrote to create a new thread. 

This ab initio thread is called the main thread. Under normal conditions, 
the main thread is the thread from which the Python interpreter was started. 

Notice the debugger dropdown displays two threads:

1. Main Thread
2. demoThread
"""
