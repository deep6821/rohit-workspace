"""
RLock:
------
- A reentrant lock is defined as a lock which can be reacquired by the same
  thread.
- A RLock object carries the notion of ownership. If a thread acquires a RLock
  object, it can chose to reacquire it as many times as possible. Consider the
  following snippet:

  # create a reentrant lock
  rlock = RLock()

  # acquire the lock twice
  rlock.acquire()
  rlock.acquire()

  # release the lock twice
  rlock.release()
  rlock.release()


In contrast to Lock, the reentrant lock is acquired twice in the above snippet
without blocking. Note that it is imperative to release the lock as many times
as it is locked, otherwise the lock remains in locked state and any other
threads attempting to acquire the lock get blocked. """

from threading import RLock
from threading import Thread


def child_task():
    rlock.acquire()
    print("child task executing")
    rlock.release()


rlock = RLock()
rlock.acquire()
rlock.acquire()
rlock.release()
# UNCOMMENT THE FOLLOWING LINE TO MAKE THE PROGRAM EXIT NORMALLY.
rlock.release()

thread = Thread(target=child_task)
thread.start()
thread.join()

"""
The nested acquire/release calls are tracked internally by recursion level 
which is incremented on every acquire() and decremented on every release() by 
the same thread. When the recursion level is zero, the reentrant lock is in 
unlocked state.
"""
