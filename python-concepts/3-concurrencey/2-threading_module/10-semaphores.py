"""
Semaphores:
-----------
- Semaphore is one of the oldest synchronization primitives, invented by Edsger
  Dijkstra.
- A semaphore is nothing more than an atomic counter that gets decremented by
  one whenever acquire() is invoked and incremented by one whenever release()
  is called.
- The semaphore can be initialized with an initial count value. If none is
  specified, the semaphore is initialized with a value of one.
"""