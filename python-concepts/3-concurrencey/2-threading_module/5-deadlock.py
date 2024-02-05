import time
from threading import Lock
from threading import Thread
from threading import current_thread

print(" ------------------------ Deadlock Example ---------------------")
# Consider the example below, where two threads are instantiated and each tries
# to invoke release() on the lock acquired by the other thread, resulting in a
# deadlock.


def thread_one(lock1, lock2):
    lock1.acquire()
    time.sleep(1)
    lock2.release()


def thread_two(lock1, lock2):
    lock2.acquire()
    time.sleep(1)
    lock1.release()


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=thread_one, args=(lock1, lock2))
    t2 = Thread(target=thread_one, args=(lock1, lock2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
